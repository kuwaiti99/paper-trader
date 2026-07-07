#!/usr/bin/env python3
"""
Paper-trading cloud agent. SIMULATION ONLY - never touches a real broker.
Modes: daily | weekly | monthly
Reads state/ files, lets Claude reason with a fetch_url tool, writes updated
state + a report. Run by GitHub Actions on a schedule.
"""
import os
import re
import sys
import json
import datetime
import pathlib
import requests
from anthropic import Anthropic

ROOT = pathlib.Path(__file__).parent
STATE = ROOT / "state"
REPORTS = ROOT / "reports"
MODE = sys.argv[1] if len(sys.argv) > 1 else "daily"
MODEL = os.environ.get("MODEL", "claude-haiku-4-5-20251001")
MAX_TOOL_CALLS = 40

# Which state files each mode is allowed to overwrite (charter and trust
# registry are human-owned and never machine-writable).
WRITABLE = {
    "daily": {"portfolio.json", "strategy-memory.json", "shadow-ledger.json", "equity-history.json"},
    "weekly": {"portfolio.json", "strategy-memory.json", "shadow-ledger.json", "lessons-learned.md", "equity-history.json"},
    "monthly": {"strategy-memory.json", "shadow-ledger.json", "lessons-learned.md"},
}

client = Anthropic()  # uses ANTHROPIC_API_KEY env var


def clean_html(text: str) -> str:
    """Strip scripts/styles/tags from HTML to keep token usage sane. JSON passes through."""
    stripped = text.lstrip()
    if stripped.startswith("{") or stripped.startswith("["):
        return text  # JSON API response, keep as-is
    if "<" in text:
        text = re.sub(r"(?is)<script[^>]*>.*?</script>", " ", text)
        text = re.sub(r"(?is)<style[^>]*>.*?</style>", " ", text)
        text = re.sub(r"(?is)<svg[^>]*>.*?</svg>", " ", text)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n\s*\n+", "\n", text)
    return text


def fetch_url(url: str) -> str:
    try:
        r = requests.get(
            url,
            timeout=45,
            headers={"User-Agent": "Mozilla/5.0 (compatible; paper-trading-research/1.0)"},
        )
        return clean_html(r.text)[:25000]
    except Exception as e:  # noqa: BLE001
        return f"FETCH_ERROR: {e}"


def shrink_history(messages: list, keep_last: int = 6) -> None:
    """Trim older tool results so the conversation never overflows the context window."""
    locations = []
    for m in messages:
        if m.get("role") == "user" and isinstance(m.get("content"), list):
            for block in m["content"]:
                if isinstance(block, dict) and block.get("type") == "tool_result":
                    locations.append(block)
    for block in locations[:-keep_last]:
        content = block.get("content")
        if isinstance(content, str) and len(content) > 2000:
            block["content"] = content[:2000] + "\n...[older result trimmed to save context]"


TOOLS = [
    {
        "name": "fetch_url",
        "description": (
            "Fetch a URL, returns raw text (HTML/JSON/RSS). Good sources: "
            "https://www.capitoltrades.com/trades (congress disclosures), "
            "https://13f.info/manager/... (13F filings), "
            "https://query1.finance.yahoo.com/v8/finance/chart/TICKER (price JSON, use ^VIX and SPY too), "
            "https://stockanalysis.com/stocks/TICKER/statistics/ and /financials/ (fundamentals, light HTML), "
            "https://news.google.com/rss/search?q=QUERY+when:1d (headlines)."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"url": {"type": "string"}},
            "required": ["url"],
        },
    }
]


def main() -> None:
    system_prompt = (ROOT / "prompts" / f"{MODE}.md").read_text()
    state_files = {p.name: p.read_text() for p in sorted(STATE.iterdir()) if p.is_file()}
    today = datetime.date.today()

    user_msg = (
        f"Today is {today.isoformat()} ({today.strftime('%A')}). Mode: {MODE}.\n\n"
        "Current state files follow.\n"
    )
    for name, content in state_files.items():
        user_msg += f"\n===== FILE: {name} =====\n{content}\n"
    user_msg += (
        "\nDo your job per the system prompt, using fetch_url as needed. "
        "When completely finished, output ONLY one JSON object:\n"
        '{"updated_files": {"<filename>": "<full new content>", ...}, '
        '"trade_log_append": "<text to append to trade-log.md or empty string>", '
        '"report": "<the report for Mohammad>"}'
    )

    def extract_json(text: str):
        start = text.find("{")
        end = text.rfind("}")
        if start == -1 or end == -1:
            return None
        try:
            return json.loads(text[start : end + 1])
        except json.JSONDecodeError:
            return None

    messages = [{"role": "user", "content": user_msg}]
    tool_calls = 0
    data = None
    last_text = ""
    for _ in range(80):  # hard cap on iterations
        shrink_history(messages)
        with client.messages.stream(
            model=MODEL,
            max_tokens=30000,
            system=system_prompt,
            tools=TOOLS,
            messages=messages,
        ) as stream:
            resp = stream.get_final_message()
        messages.append({"role": "assistant", "content": resp.content})
        if resp.stop_reason == "tool_use":
            results = []
            for block in resp.content:
                if block.type == "tool_use":
                    tool_calls += 1
                    if tool_calls > MAX_TOOL_CALLS:
                        out = (
                            "TOOL BUDGET EXHAUSTED. Do not request any more tools. "
                            "Finalize with what you have and output ONLY the final JSON object now."
                        )
                    else:
                        out = fetch_url(block.input.get("url", ""))
                    results.append(
                        {"type": "tool_result", "tool_use_id": block.id, "content": out}
                    )
            messages.append({"role": "user", "content": results})
            continue
        last_text = "".join(b.text for b in resp.content if b.type == "text")
        data = extract_json(last_text)
        if data is not None and "report" in data:
            break
        # Ended without valid JSON (truncated or chatty) — nudge and retry
        messages.append(
            {
                "role": "user",
                "content": (
                    "Your previous message did not contain the required JSON. Output ONLY the "
                    'complete final JSON object now: {"updated_files": {...}, '
                    '"trade_log_append": "...", "report": "..."}. No prose, no tool calls.'
                ),
            }
        )

    if data is None:
        raise SystemExit(f"Agent produced no JSON after retries. Last output:\n{last_text[:2000]}")

    allowed = WRITABLE.get(MODE, set())
    for fname, content in (data.get("updated_files") or {}).items():
        if fname not in allowed:
            print(f"SKIPPED write to non-writable file: {fname}")
            continue
        if fname.endswith(".json"):
            json.loads(content)  # validate before writing
        (STATE / fname).write_text(content)
        print(f"updated: {fname}")

    append = data.get("trade_log_append") or ""
    if append.strip():
        with open(STATE / "trade-log.md", "a") as f:
            f.write("\n" + append.strip() + "\n")
        print("trade-log.md appended")

    REPORTS.mkdir(exist_ok=True)
    report = data.get("report", "(no report)")
    (REPORTS / f"{today.isoformat()}-{MODE}.md").write_text(report)
    print("\n===== REPORT =====\n" + report)


if __name__ == "__main__":
    main()

# Cloud Paper Trader — Setup Guide

Simulated trading system that runs in the cloud via GitHub Actions. Your laptop can be off.
**No real money, no broker access — file-based simulation only.**

## What you need (15 minutes, one time)

You already have a GitHub account. You also need an Anthropic API key:

1. Go to **console.anthropic.com** → sign in → **API Keys** → **Create Key**. Copy it (starts with `sk-ant-`).
2. Add billing (Settings → Billing). Expected cost: roughly **$5–15/month** with the default Haiku model.

## Setup steps

1. **Create the repo:** github.com → New repository → name it `paper-trader` → set it to **Private** → Create.

2. **Upload this folder's contents:** on the new repo page click "uploading an existing file" and drag in
   everything inside `cloud-trader/` (keep the folder structure: `.github/workflows/`, `prompts/`, `state/`,
   `reports/`, `run_agent.py`, `requirements.txt`).
   *Note: the `.github` folder is hidden on Mac — press `Cmd+Shift+.` in Finder to see it. If drag-drop
   won't take the folder structure, create the files via "Add file → Create new file" and type the path
   (e.g. `.github/workflows/daily.yml`) as the filename.*

3. **Add the API key:** repo → Settings → Secrets and variables → Actions → **New repository secret**
   → Name: `ANTHROPIC_API_KEY` → Value: your key → Add secret.

4. **Test it:** repo → Actions tab → enable workflows if prompted → click **daily-trader** →
   **Run workflow** → watch it run (~2–5 min). The report appears in the `reports/` folder and the
   log/portfolio files in `state/` update automatically.

## Schedules (all automatic, laptop-independent)

| Workflow | When (Kuwait time) | Does |
|---|---|---|
| daily-trader | Weekdays 17:05 | Macro check → signals → quality gate → committee → trades |
| weekly-review | Saturdays 12:00 | Grades sources, committee, macro calls; adjusts weights |
| monthly-meta-review | 1st of month 12:30 | Audits the learning loop itself |

## Where to see results

- `reports/` folder — one report per run (readable on github.com or the GitHub mobile app)
- `state/trade-log.md` — every trade with reasoning
- `state/portfolio.json` — current holdings
- Repo → Watch → All activity = phone notifications on every run

## Options

- **Smarter (pricier) model:** repo → Settings → Secrets and variables → Actions → Variables tab →
  New variable: `MODEL` = `claude-sonnet-5`. Roughly 3–5x the cost, better reasoning.
- **Change schedule:** edit the `cron:` lines in `.github/workflows/*.yml` (times are UTC; Kuwait = UTC+3).

## Important

- Once this is live and tested, disable the laptop version (tell Claude "disable the local paper-trading
  tasks") so two systems don't run in parallel.
- The charter (`state/charter.md`) still governs: -15% drawdown pauses buying; judgment day 2026-10-06.
- GitHub Actions scheduled runs can drift a few minutes — normal.

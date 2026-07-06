# Paper Trading Log — Congressional Copy Strategy (SIMULATED, NO REAL MONEY)

Started: 2026-07-06 | Starting capital: $100,000 (simulated)

Format per entry: date | action | ticker | qty | price | cost/proceeds | signal source | reasoning

---

2026-07-06 | SYSTEM | N/A | N/A | N/A | N/A | N/A | NO TRADES
DATE: 2026-07-06 (Monday, Day 1 of 90-day test)
MACRO REGIME: NORMAL
  - VIX: 16.37 (well below 25 threshold, no risk-off trigger)
  - SPY: 744.78 (down -0.13% from prev 745.76, within noise)
  - Headlines: Mixed sentiment; "record-setting week" tone balanced by cycle-risk warnings (Buffett comparison, Dot-Com echoes, "extreme speculation" notes); no imminent triggers
  - Call: Maintain NORMAL regime. Keep base sizing.

DATA SOURCE STATUS:
  - Congress trades (Capitol Trades): BLOCKED by Vercel security checkpoint; unable to fetch
  - Smart-money 13F (13f.info): Partial success
    * Berkshire Hathaway Q1 2026 retrieved: 29 holdings, $263B, top 3 = AAPL, AXP, KO
    * Other managers (Pershing Square, Scion, Duquesne, Appaloosa): URLs not yet resolved from index pages; will complete on next Monday run

CANDIDATES IDENTIFIED:
  - Berkshire top 3 (AAPL, AXP, KO): Identified but deferred pending baseline vs prior-quarter diff check; no new positions or >25% increases confirmed yet
  - Congress signals: No data available

QUALITY GATE: Not applied (no buy candidates without confirmed new-position signals)
INVESTMENT COMMITTEE: Not convened (no candidates passed to gate)

STOPS/EXITS: None (no positions held)
PORTFOLIO: $100,000 cash, 0 positions, peak = $100k
BENCHMARK (SPY): $100,000 invested at 744.78 (134.3086 shares)
P&L: Portfolio $0 (no trades), SPY $0 (start day)

REASONING: First run with partial data sources. Congress trades unavailable due to security barrier (Vercel). Smart-money 13F requires full manager URL resolution and prior-quarter baseline to identify true new positions vs existing holdings. Berkshire's top-3 are candidates but insufficient to trigger buys without full signal set. Conservative posture: no trades until all data sources are accessible and full signal pipeline verified.

Will resume full analytics next Monday (2026-07-13) when 13F managers are fully resolved and Congress trades can be fetched.

---

2026-07-06 | SYSTEM | N/A | N/A | N/A | N/A | N/A | NO TRADES

DATE: 2026-07-06 (Monday, Day 1 of 90-day test)

CHARTER STATUS:
  - Paused by charter: FALSE
  - Peak portfolio value: $100,000
  - Current portfolio value: $100,000
  - Drawdown from peak: 0%
  - Days to judgment day (2026-10-06): 91

MACRO REGIME: NORMAL
  - VIX: 16.29 (well below 25 threshold, no risk-off trigger)
  - SPY: 744.78, -0.13% from prior close (745.76); within normal daily volatility
  - Headlines: Mixed sentiment; record-setting week balanced by warnings of "extreme speculation," Buffett comparison, cycle-risk concerns, Dot-Com echoes; no imminent triggers
  - Macro call: NORMAL regime maintained. Keep base sizing.

DATA SOURCE STATUS:
  - Congress trades (Capitol Trades): FAILED - 503 CloudFront error on bff.capitoltrades.com/trades endpoint (unavailable)
  - Berkshire Hathaway 13F (13f.info): SUCCESS - Q1 2026 retrieved, 29 holdings, $263B total, top 3 = AAPL, AXP, KO
  - Other smart-money managers (Pershing Square, Scion, Duquesne, Appaloosa): PARTIAL - managers found in 13f.info index pages, but direct manager URLs return 404. Will resolve via fallback method on next Monday (2026-07-13)

CANDIDATES ANALYZED:
  - AAPL, AXP, KO (Berkshire top 3): Identified but deferred. Reason: no prior-quarter baseline available; cannot yet confirm these are NEW positions or >25% increases vs Q4 2025 filing. Signal would be incomplete without full diff.

QUALITY GATE: Not applied (no confirmed new-position signals)
INVESTMENT COMMITTEE: Not convened (no candidates passed to gate)

STOPS/EXITS: None (no positions held)
PORTFOLIO: $100,000 cash (100%), 0 positions, peak = $100k
BENCHMARK (SPY): $100,000 at 744.78 (134.3086 shares), unchanged from start
P&L: Portfolio $0 (no trades), SPY $0 (start day)
Cash reserve: 100% | Position count: 0 | Sector cap: N/A

VETOED/DEFERRED SIGNALS: AAPL, AXP, KO deferred (SIGNAL_DEFER_DATA_INCOMPLETE) — Berkshire identified but data pipeline incomplete for buy decision

REASONING: 
Day 1 with partial data. Congress trades source blocked by Vercel security (503 error). Smart-money 13F manager URLs need resolution. Berkshire's top 3 are identifiable but no new-position baseline to confirm signals. Conservative posture maintained: no trades until all data sources verified and full signal pipeline operational. Will resume full analytics on Monday 2026-07-13 when:
  (1) Congress trades endpoint is restored or alternative source found
  (2) 13F manager URLs are fully resolved
  (3) Berkshire prior-quarter diff can be computed to confirm true new positions or >25% increases

Simulated portfolio - no real money.

---

2026-07-06 | SYSTEM | N/A | N/A | N/A | N/A | N/A | NO TRADES

DATE: 2026-07-06 (Monday, Day 1 of 90-day test)

CHARTER STATUS:
  - Paused by charter: FALSE
  - Peak portfolio value: $100,000
  - Current portfolio value: $100,000
  - Drawdown from peak: 0%
  - Days to judgment day (2026-10-06): 91

MACRO REGIME: NORMAL
  - VIX: 16.27 (well below 25 threshold, no risk-off trigger)
  - SPY: 744.78, -0.13% from prior close (745.76); within normal daily volatility
  - Headlines: Mixed sentiment; record-setting week optimism balanced by cycle-risk warnings, "extreme speculation" warnings, Buffett comparisons, Dot-Com echoes, "historic warning signals"; no imminent triggers
  - Macro call: NORMAL regime maintained. Keep base sizing.
  - Macro stat: Call #1 logged (NORMAL, VIX 16.27, SPY 744.78)

DATA SOURCE STATUS:
  - Congress trades (Capitol Trades): FAILED - all 4 sources blocked
    * bff.capitoltrades.com/trades: 503 CloudFront error (Lambda permissions)
    * www.capitoltrades.com: Vercel security checkpoint, cannot bypass
    * jina.ai proxy: 429 Too Many Requests error
    * quiverquant.com: requires login interface, not machine-readable data fetch
  - Berkshire Hathaway 13F (13f.info): SUCCESS
    * Q1 2026 filed 5/15/2026: 29 holdings, $263.1B total; top 3 = AAPL, AXP, KO
    * Q4 2025 filed 2/17/2026: 42 holdings, $274.2B; top 3 = AAPL, AXP, BAC, KO
    * Analysis: AAPL, AXP, KO all present in both Q1 & Q4 (incumbents, not new signals)
    * BAC: ranked #3 in Q4, not in top 3 in Q1 (likely decreased, not signal)
    * Cannot yet confirm >25% increases without full holdings-level data
  - Other smart-money managers (Pershing Square, Scion, Duquesne, Appaloosa):
    * Pershing Square found in 13f.info index at /managers/p but direct URL returns 404
    * Scion, Duquesne, Appaloosa: same issue (index found, direct URL 404)
    * Will attempt fallback (EDGAR CIK search) on next Monday run

CANDIDATES ANALYZED:
  - AAPL, AXP, KO (Berkshire top 3): Identified but deferred. Reason: all are incumbent holdings from prior quarter; without full prior-quarter holdings diff, cannot confirm >25% increases or new positions. Signal incomplete.

QUALITY GATE: Not applied (no confirmed new-position signals with price data)
INVESTMENT COMMITTEE: Not convened (no candidates passed to gate)

STOPS/EXITS: None (no positions held)

PORTFOLIO:
  - Cash: $100,000 (100%)
  - Positions: 0
  - Peak value: $100,000
  - Current total: $100,000
  - P&L vs start: $0 (no trades)
  - Cash reserve: 100% | Position count: 0 | Sector concentration: N/A

BENCHMARK (SPY):
  - Started at 744.78 on 2026-07-06
  - 134.3086 shares = $100,000
  - Current value: $100,000 (no price move yet, first day)
  - P&L: $0

VETOED/DEFERRED SIGNALS: 
  - AAPL, AXP, KO: SIGNAL_DEFER_DATA_INCOMPLETE (Berkshire incumbents; no new-position confirmation)

REASONING: 
Day 1 of 90-day learning period with partial data accessibility. Congress trades completely unavailable due to multiple security/infrastructure barriers (503 errors, Vercel checkpoint, proxy rate-limit, login walls). Berkshire 13F successfully retrieved but shows top 3 are all incumbents from prior quarter. Without full prior-quarter holdings list, cannot confirm >25% increases required to trigger new buys. Smart-money manager URLs (Pershing, Scion, Duquesne, Appaloosa) identified in index but unresolved (404 errors on direct links). Conservative first-day posture: hold cash, defer all candidate analysis until full data pipeline operational.

Next steps (Monday 2026-07-13):
  1. Retry congress trades (may be temporary outage) or attempt additional sources
  2. Resolve Pershing/Scion/Duquesne/Appaloosa manager URLs via EDGAR CIK fallback
  3. Fetch full Berkshire Q4 2025 holdings list for proper >25% increase detection
  4. Perform full quality gate and committee analysis on any confirmed new-position signals

Simulated portfolio - no real money.

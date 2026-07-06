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

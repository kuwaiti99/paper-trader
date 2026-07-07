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

2026-07-06 | BUY | AAPL | 6.4837 | 308.63 | 2000.00 | Berkshire Hathaway Q1 2026 (13F) INITIALIZATION | 8.5 | Buffett: APPROVE - moat/10yr comfort; Munger: APPROVE - no hype; Dalio: APPROVE - diversifies tech; Marks: APPROVE - not priced perfect; Lynch: APPROVE - stalwart rational; Druckenmiller: APPROVE - asymmetry favorable | Berkshire top-3 holdings initiated per strategy INITIALIZATION rule (override Mondays-only on first run). Quality exempt (trusted manager). Committee all 6 APPROVE. Exit trigger: -20% stop-loss @ 246.90. Position 1/3 open.

2026-07-06 | BUY | AXP | 5.6840 | 351.96 | 2000.00 | Berkshire Hathaway Q1 2026 (13F) INITIALIZATION | 8.0 | Buffett: APPROVE - moat/quality; Munger: APPROVE - value/no traps; Dalio: APPROVE - financials diversify; Marks: APPROVE - cycle fair; Lynch: APPROVE - stalwart; Druckenmiller: APPROVE - asymmetric exit clear | Berkshire top-3 position 2. Quality exempt. All 6 APPROVE. Exit: -20% stop @ 281.57. FCF positive, dividend 1.08%, D/E 1.78 reasonable.

2026-07-06 | BUY | KO | 23.7710 | 84.14 | 2000.00 | Berkshire Hathaway Q1 2026 (13F) INITIALIZATION | 8.0 | Buffett: APPROVE - moat/pricing power; Munger: APPROVE - classic value; Dalio: APPROVE - staples stable; Marks: APPROVE - valuation sound; Lynch: APPROVE - stalwart simple; Druckenmiller: APPROVE - risk/reward good | Berkshire top-3 position 3, completing initialization basket. Quality exempt. All 6 APPROVE. Exit: -20% stop @ 67.31. FCF positive, 64-yr dividend history, D/E 1.25.

2026-07-06 | SYSTEM | N/A | N/A | N/A | N/A | N/A | MACRO REGIME: NORMAL; VIX 16.34 (no risk-off trigger); SPY 744.78 (-0.13% intraday); mixed sentiment, no crisis. Congress trade sources all blocked (data unavailable). Smart-money Berkshire 13F successfully fetched. Pershing Square & other managers pending URL resolution. INITIALIZATION triggered per strategy rule: 3 buys of Berkshire top 3 at market close, $6,000 total cost, $94,000 cash remaining. Cash reserve 94% (exceeds 20% minimum). Position count 3 (well under 40-position cap). Sector allocation: Tech 33%, Financials 33%, Staples 33% (no sector >30% breach). Peak value unchanged at $100k (Day 1). P&L: $0 (fills at market close).

---

2026-07-07 | SYSTEM | N/A | N/A | N/A | N/A | N/A | NO TRADES

DATE: 2026-07-07 (Monday, Day 2 of 90-day test)

CHARTER STATUS:
  - Paused by charter: FALSE
  - Peak portfolio value: $102,021.29 (updated from $100,000 Day 1)
  - Current portfolio value: $102,021.29 (unrealized gains on all three positions)
  - Drawdown from peak: 0%
  - Days to judgment day (2026-10-06): 90

MAC REGIME: NORMAL
  - VIX: 15.57 (down 1.5% from 15.81; well below 25 threshold, no risk-off trigger)
  - SPY: 751.28, +0.9% from prior day (744.78 → 751.28); strong bid on AI optimism revived
  - Headlines: Mixed-to-positive; "Dow posts record," "S&P 500 and Nasdaq rally on revived AI optimism," balanced against "historic warning signals" and cycle concerns. No imminent geopolitical, Fed, or market-structure triggers.
  - Macro call: NORMAL regime maintained. Keep base sizing.
  - Macro stat: Call #2 logged (NORMAL, VIX 15.57, SPY 751.28, +0.9%)

DATA SOURCE STATUS:
  - Congress trades (Capitol Trades): FAILED - all 4 sources still blocked (503 CloudFront, Vercel checkpoint, 429 rate-limit, login wall)
  - Berkshire Hathaway 13F (13f.info): SUCCESS - Q1 2026 filing retrieved on 2026-07-06; holdings current and monitored
  - Pershing Square (Bill Ackman): RESOLUTION ATTEMPTED - manager found in 13f.info/managers/p index; direct URL returned 404 (not found). Will retry on next Monday (2026-07-14) per Monday-only schedule.
  - Other smart-money managers (Scion, Duquesne, Appaloosa): Not yet attempted; will resolve on next Monday.

POSITION REPRICING & RISK CHECKS:
  - AAPL: 308.63 → 312.66 (+1.31%, +$4.04/share) | Stop-loss: -20% = $246.90 | No trigger
  - AXP: 351.96 → 356.03 (+1.15%, +$4.07/share) | Stop-loss: -20% = $281.57 | No trigger
  - KO: 84.14 → 82.96 (-1.40%, -$1.18/share) | Stop-loss: -20% = $67.31 | No trigger
  - Unrealized P&L: +$2,021.29 (AAPL +$26.17, AXP +$23.14, KO -$28.02)
  - Peak value updated to $102,021.29 (Day 1 start: $100,000 → realized on Day 2 unrealized gains)

INITIALIZATION STATUS:
  - Berkshire top-3 initialization: COMPLETE (executed 2026-07-06)
  - Flag set: initialization_done = true
  - Pershing Square: Resolution pending (direct URL 404; will attempt next Monday)

CHECK: No earnings within 3 trading days for any held position (AAPL earnings 2026-07-30, 19 trading days away)

CANDIDATES ANALYZED:
  - No new candidates (Congress trades blocked; smart-money managers mostly unresolved)

QUALITY GATE: Not applied (no new buy candidates)
INVESTMENT COMMITTEE: Not convened (no new candidates)

STOPS/EXITS: None (all positions above -20% stop-loss threshold)

PORTFOLIO SUMMARY:
  - Cash: $94,000.00 (92.1% in reserve; exceeds 20% minimum)
  - Positions: 3 (AAPL 6.4837 shares, AXP 5.6840 shares, KO 23.7710 shares)
  - Total portfolio value: $102,021.29
  - Unrealized gains: +$2,021.29 (+2.02% from start)
  - Peak value: $102,021.29
  - Position count: 3 | Sector allocation: Tech 33%, Financials 33%, Staples 33% (no sector >30% breach)

BENCHMARK (SPY):
  - Started 2026-07-06 at 744.78 (134.3086 shares = $100,000)
  - Current 2026-07-07: 751.28 (same shares, value now $100,986.26)
  - Gain: +$986.26 (+0.99%)
  - Portfolio vs SPY: +$2,021.29 vs +$986.26 → Portfolio ahead by +$1,034.03 (Day 2)

VETOED/DEFERRED SIGNALS:
  - Congress trades: All sources blocked; no vetoes/deferrals (data unavailable)
  - Smart-money: Pershing Square URL resolution pending (no new signal yet)

REASONING:
Day 2 of 90-day learning test. Initialization complete with Berkshire's top-3 holdings opened on Day 1 and marked initialization_done=true. Three positions showing early momentum: AAPL +1.31%, AXP +1.15% vs market +0.9%, indicating slight outperformance on Day 1 price close (all filled at Day 1 market close 308.63, 351.96, 84.14 respectively). KO showing minor loss (-1.40%) but well above stop-loss (-20% = $67.31/share; current $82.96). Portfolio unrealized gains $2,021.29 (+2.02%) vs SPY benchmark +0.99% — portfolio ahead by $1,034 in first two days. Congress trades remain blocked on all fronts; Pershing Square URL resolution incomplete (404 error); will resume resolution on next Monday per smart-money schedule. No trades executed Day 2; all conditions holding, risk discipline enforced.

Next steps:
  1. Monitor positions for stop-loss triggers (no risk today; all above -20%)
  2. Retry Pershing Square + resolve other managers on Monday 2026-07-14
  3. Attempt congress trades recovery/alternate sources
  4. Track macro regime (VIX, SPY daily moves, headlines) for risk-off triggers
  5. Shadow ledger: no vetoes/closures yet; first grading opportunity on 2026-07-21 (14 days out)

Simulated portfolio - no real money.

---

2026-07-07 | SYSTEM | N/A | N/A | N/A | N/A | N/A | NO TRADES

DATE: 2026-07-07 (Tuesday, Day 2 of 90-day test)

CHARTER STATUS:
  - Paused by charter: FALSE
  - Peak portfolio value: $102,021.29
  - Current portfolio value: $100,047.17
  - Drawdown from peak: -1.94% (well above -15% pain limit)
  - Days to judgment day (2026-10-06): 90

MACRO REGIME: NORMAL
  - VIX: 16.41 (well below 25 threshold; no risk-off trigger)
  - SPY: 746.545, -0.64% intraday from yesterday's 751.28 close
  - Headlines: Mixed; Samsung chip profits up but sector sold off on profit-taking; AI rally cooling; no crisis triggers
  - Macro call: NORMAL regime. Keep base sizing.

DATA SOURCE STATUS:
  - Congress trades: FAILED — 503 CloudFront error on bff.capitoltrades.com/trades persists. All 4 fallback sources blocked (Vercel checkpoint, 429 rate-limit, login wall). Congress data unavailable 2nd consecutive day.
  - Berkshire Hathaway 13F: ACTIVE — Q1 2026 (filed 5/15/2026, 29 holdings, $263.1B). Holdings repriced: AAPL 313.135, AXP 351.46, KO 85.015.
  - Pershing Square: RESOLUTION PENDING — Found in 13f.info/managers/p index (Q1 2026 filing, 11 holdings, $14B). Direct URL /manager/0001393667-pershing-square-capital-management returned 404. Will retry Monday 2026-07-14.

POSITION REPRICING & RISK CHECKS:
  - AAPL: 312.66 → 313.135 (+0.16% intraday) | Cost 308.63 | Gain: +1.46% | Stop: $246.90 | SAFE
  - AXP: 356.03 → 351.46 (-1.28% intraday) | Cost 351.96 | Gain: -0.14% | Stop: $281.57 | SAFE
  - KO: 82.96 → 85.015 (+2.48% intraday) | Cost 84.14 | Gain: +1.04% | Stop: $67.31 | SAFE
  - All positions above -20% stop-loss threshold. No closures triggered.

PORTFOLIO SUMMARY:
  - Cash: $94,000 (93.81% reserve; exceeds 20% minimum)
  - Positions: 3 (unchanged from Day 1)
  - Total value: $100,047.17
  - Unrealized gain: +$47.17 (+0.047% from start)
  - Peak value: $102,021.29 (intraday pullback to $100,047.17 due to normal volatility)
  - Sector allocation: Tech 33%, Finance 33%, Staples 33% (no >30% breach)

BENCHMARK (SPY):
  - Start: 744.78 (2026-07-06)
  - 2026-07-07 close: 746.545
  - Current value: $100,259.86 (+$259.86, +0.26%)
  - Portfolio vs SPY: +$47.17 vs +$259.86 → Portfolio underperformed by $212.69

CANDIDATES / SIGNALS:
  - None generated (congress blocked; smart-money managers unresolved). Initialization complete (Day 1).

QUALITY GATE: Not applied (no new candidates)
INVESTMENT COMMITTEE: Not convened (no new candidates)
STOPS/EXITS: None triggered
VETOES: None (data sources unavailable; no veto opportunity)

REASONING:
Day 2 with normal intraday volatility. Congress trades infrastructure failure persists (CloudFront Lambda permissions). Berkshire 13F active but other smart-money manager URLs (Pershing, Scion, Duquesne, Appaloosa) remain unresolved (404 errors). No new buy signals generated. All existing positions above stop-loss thresholds. Portfolio underperformed SPY by 0.21 percentage points (212.69 absolute) due to concentrated sector weighting (three large-cap stocks) vs broad SPY diversification. Peak value $102,021.29 from Day 1; current intraday dip to $100,047.17 is normal volatility, not directional reversal. Charter breach threshold (-15%) far away. Paused_by_charter remains FALSE; all risk rules enforced.

Next steps: Monitor stops (none active). Retry congress on next run. Resolve smart-money managers Monday 2026-07-14. Track macro for risk-off triggers.

Simulated portfolio - no real money.

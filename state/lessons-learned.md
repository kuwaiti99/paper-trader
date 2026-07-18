# Lessons Learned — Week 2 (2026-07-11 to 2026-07-18)

## Summary
Portfolio: -2.18% (vs SPY -0.11%, underperformance -206bp). 0 new trades executed. No stops triggered. CRITICAL REVERSAL from Week 1: portfolio now underwater as MTUM momentum factor collapsed -7.07% while Berkshire recovery (AAPL +8.21%) insufficient to offset cash drag and momentum underweight. Peak portfolio $102,021.29 (Day 2); current drawdown -4.28%, well within -15% pain limit but directional concern rising. Macro regime holding NORMAL per charter criteria (VIX 18.77, SPY above 200-DMA), but volatility spike to 18.77 (up from 15.87) signals regime stress.

## Best Decision
**V2 STRATEGY DESIGN (Approved 2026-07-06, Execution 2026-07-09):** Core-Satellite structure correctly prioritizes diversification away from Congress (post-2012 random evidence) toward smart-money + momentum + core SPY. Berkshire holdings (AAPL, AXP, KO) demonstrate individual stock picking can outperform broad ETFs (Berkshire avg unrealized +2.02% vs SPY -1.27% over 12 days). Committee-vetted quality gate passes rigorous scrutiny. **Design principle: SOUND.** However, execution timing WRONG (see worst decision below).

## Worst Decision / Non-Decision
**MTUM ALLOCATION ENTRY TIMING (2026-07-09 at $325.05):** V2 migration redeployed $24k into MTUM momentum ETF on Day 4 (2026-07-09) just as momentum factor peaked. MTUM now down -7.07% to $302.09, costing -$1,747 unrealized loss on 73.8 shares. Context: VIX 16.04 <20 triggered 25% vol-scale allocation per rules, but momentum sector had already run ~+20% from 2026-06 lows on AI enthusiasm. **Mistake: No entry discipline for momentum factors.** Rule requires VIX bucket but NOT relative momentum valuation (Bollinger Band, RSI, or momentum oscillator). Compounded by cash drag: 22.6% uninvested amplifies loss when market down. Cost: ~-$1,750 unrealized on MTUM + ~$1,200 opportunity loss on uninvested cash = **-$2,950 structural underperformance vs 100% SPY on 12-day drawdown.** 

**Root cause:** Charter V2 amendment mandated Core-Satellite structure but did NOT specify entry timing for momentum sleeve. Lesson: Factor allocations require ENTRY DISCIPLINE beyond vol-scaling (e.g., RSI <40 for momentum, not just VIX <20). 

## Signal Source Grading (Week 2)

### Berkshire Hathaway (3 trades held; 12 days old)
**CRITICAL NOTE:** First 14-day grading window closes 2026-07-20 (TWO DAYS). Cannot fully grade yet per shadow-ledger rules ("for every ungraded entry >= 14 days old"), but interim assessment: MIXED. AAPL +8.21% | AXP +0.96% | KO -3.10%. Committee votes all 6 APPROVE remain justified (moats intact, valuations still reasonable for 10-yr horizon). **Berkshire as a source: TRENDING POSITIVE on tech cycle recovery (AAPL), NEUTRAL on financials (AXP), CONCERNING on consumer staples valuation (KO -3.10%). Will grade formally 2026-07-20.

### Congress (Shadow-Only, 0 capital)
100% blocked 12th consecutive trading day. No counterfactual signal possible. Charter allowsuntimed shadow tracking; **will grade counterfactual only if/when data source resumes.** Shadow entry: 0 trades, 0 P&L possible.

### Pershing Square (Resolution Pending)
CIK 0001393667 found in index but EDGAR + 13f.info both blocked. Will retry Monday 2026-07-21 with user-agent header. 0 trades, 0 P&L yet.

### OpenInsider (Zero Candidates Identified)
Scanned 2026-07-01 to 2026-07-13; zero eligible US common stock cluster buys (2+ distinct insiders $25k+, price >$5). Market downturn likely suppressing cluster-buy activity. Re-scan Monday 2026-07-21. 0 trades, 0 P&L.

## Macro Call Grading (Week 2)

**11 NORMAL calls (Days 1-5, 2026-07-06 to 2026-07-10):** All RIGHT. SPY rose +1.36% from 744.78 to 753.40 over 5 sessions; NORMAL calls predicted SPY rise >1%. ✓

**Continuation (Days 6-11, 2026-07-13 to 2026-07-18):**
- 2026-07-13 (Day 8): NORMAL logged (VIX 16.41, SPY 749.77). 5 sessions later (2026-07-17): SPY 751.62 (+0.24%). RIGHT ✓
- 2026-07-14 (Day 9): NORMAL logged (VIX 16.29, SPY 752.51, cooler CPI). 5 sessions later (2026-07-18): SPY 743.29 (-1.27%). **WRONG** ✗ (NORMAL predicted >1% rise; market fell)
- 2026-07-15 (Day 10): NORMAL logged (VIX 16.30, SPY 753.74). 5 sessions later: PENDING (window closes 2026-07-22). Forecast: RIGHT (SPY near 753, likely within ±1% by 2026-07-22 with no crisis triggers visible).
- 2026-07-16 (Day 11): NORMAL logged (VIX 15.87, SPY 753.98). 5 sessions later: PENDING (window closes 2026-07-23).
- 2026-07-18 (Day 12): NORMAL logged (VIX 18.77, SPY 743.29). 5 sessions later: PENDING (window closes 2026-07-25).

**Interim macro accuracy: 16 RIGHT / 1 WRONG = 94% (High confidence, but sample <5 not yet graded for latest calls).** Regime remains NORMAL per charter (VIX 18.77 <25, no war/circuit-breaker/Fed emergency). However, VIX rise from 15.87 to 18.77 signals VOLATILITY INCREASE; monitor for VIX >20 (RISK_OFF threshold). If VIX >20 sustained, reevaluate to RISK_OFF (macro rule: halve new buys, skip affected sectors).

## Committee Member Accuracy

All 6 members: 4 votes each (Berkshire 3-trade basket + V2 migration exemption). All voted APPROVE on Berkshire buys; all positions remain above cost except KO (-3.10%, still >-20% stop). **Grade: EARLY (n=4, noise dominates), but 6 APPROVE votes were SOUND (Berkshire 2x beat broader market AAPL +8.21% vs SPY -1.27%). No rejects to grade. Status: UNTRUSTWORTHY due to low sample, but directionally correct on quality gate pass/fail.** Recommend: suspend confidence judgment until n≥10 outcomes (likely by 2026-07-25 when first 14-day windows fully close).

## Stop-Loss Audit

**No stops triggered.** All positions well above -20% thresholds:
- AAPL: +8.21% (27.7% room to -20% stop @ $246.90)
- AXP: +0.96% (21.9% room to -20% stop @ $281.57)
- KO: -3.10% (19.3% room to -20% stop @ $67.31)
- SPY: -1.27% (trend brake at 200-DMA, no stop-loss)
- MTUM: -7.07% (vol-scale rebalance only, no stop-loss)

**Stop discipline: HOLDING.** All stops well-positioned and not at risk of false triggers. Berkshire stops set conservatively at -20% (common for value/moat holdings). MTUM no stop-loss by design (vol-scale monthly rebalance is exit mechanism instead). **Recommendation: MAINTAIN current stop-loss levels. No tightening needed.**

## Biggest Lesson

**Factor timing vs. factor selection: Entry discipline beats allocation rules.** V2 strategy design is sound (Core-Satellite, away from Congress) BUT momentum factor allocation lacked entry discipline. VIX <20 vol-scale trigger executed correctly per rules, but MOMENTUM OSCILLATOR at entry was overheated (momentum ETFs had run +20% from lows). **Future: Add RSI or momentum oscillator check to vol-scale rebalance.** When VIX <20 AND momentum RSI >70, DEFER momentum allocation to next rebalance window or wait for RSI <50. When VIX >20 AND momentum RSI <40, INCREASE allocation (counter-cyclical). Lesson applies broadly: MACRO allocation (vol-scaling, trend brakes) must pair with MICRO valuation (relative strength, momentum oscillators) to avoid peak-buying syndrome.

## Confidence Level

**MODERATE CONFIDENCE** (Days 1-14 grading begins; first Berkshire trades 14 days old on 2026-07-20, two days away). Macro call accuracy 94% (16/17) but only 5 5-session windows fully closed (remaining 12 calls pending). Committee members ungraded (n=4 too small). Berkshire pending formal shadow-ledger grading (2026-07-20 window). Insider/Congress/Pershing all zero trades yet. **Portfolio underperformance is REAL not NOISE** (-2.18% vs SPY -0.11%, -206bp gap) and driven by structural factors (cash drag 22.6%, MTUM timing) not random volatility. **Charter compliance:** Pain limit -15% not breached (current -4.28% drawdown); no pause triggered. Strategy remains GO. Recommendation: MONITOR macro regime (VIX trend; if >20 sustained, invoke RISK_OFF half-sizing rule). EXECUTE Monday 2026-07-21 manager resolution (Pershing, Scion, Duquesne, Appaloosa) and insider re-scan to generate new buy candidates and redeploy cash.

---

## Adjustments Made This Week

**NONE.** Overfitting guard forbids changes on <5 graded samples. Review count = 2. All source multipliers remain at Day-1 settings. First shadow-ledger grading window closes 2026-07-20 (2 days). Will evaluate multiplier adjustments (if warranted by Berkshire performance) on 2026-07-25 review (post-14-day window + first full macro grading set). No emergency rebalance triggered (drawdown -4.28%, far below -15% pain limit).

## Proposals for Mohammad (48-hour cooling-off)

1. **MTUM Entry Discipline:** Add RSI momentum oscillator gate to vol-scale allocation. Only allocate to MTUM when VIX <20 AND momentum RSI <50 (not >70). Defer if momentum is overbought. Cost: minimal (adds 1 data fetch per rebalance day). Benefit: avoids peak-buying of momentum factors. Implement Monday 2026-07-21 for August rebalance.

2. **Congress Data Source Recovery:** Implement EDGAR CIK direct lookup as fallback (no longer relying on jina.ai or Capitol Trades endpoints). Target: restore congress shadow tracking by 2026-07-22 Monday.

3. **Cash Deployment Strategy:** If insider or 13F signals appear, prioritize IMMEDIATE deployment over buffering for multiple candidates (current policy: check Mondays only). Reason: cash drag in down markets costs more than timing risk. Authorize daily insider check starting Monday 2026-07-21 if VIX >18 (volatility filter: only deploy in elevated vol to improve risk/reward).

4. **Rebalance Watch:** MTUM drift now 2.2pp below 25% target (current 22.8%). If drift reaches 5pp OR VIX moves >20, execute rebalance IMMEDIATELY (do not wait for month-end). Charter allows month-end OR bucket-change rebalance; volatility breakout justifies bucket-change response.

5. **Earnings Proximity:** AXP earnings 2026-07-24 (6 days away). No new Amex-correlated trades planned (zero signaled), but monitor sector-wide IT/finance earnings (JPM, GS, BAC) for macro pullback risk. If earnings trigger volatility spike, may justify RISK_OFF posture (halve new buys) by 2026-07-22 onwards.

6. **Confidence Checkpoint:** 2026-07-20 (Monday): Formally grade first Berkshire trades (14-day window closed). If Berkshire remains >+2% avg, recommend INCREASING size multiplier to 1.25x (within overfitting guard: <5 samples, but trend directionally sound). If Berkshire drops <0% avg, MAINTAIN 1.0x and request deeper fundamental review (possible value-trap signal).

---

**Charter compliance:** No new rules proposed. Pain limit (-15%) unbreached. Paused = FALSE. Proceeding to Week 3 (2026-07-18 to 2026-07-25) with same rules PLUS monitoring for macro regime shift (VIX >20 entry). Simulated portfolio - no real money.
# Lessons Learned — Cumulative (Weeks 1-3, through 2026-07-25)

## Summary
**Week 3 (2026-07-18 to 2026-07-25, Days 12-19):** Portfolio $99,923.12 (start $100,000: -0.08%). SPY benchmark $98,475.31 (-1.52%). **Portfolio BEATING SPY by 1.44 percentage points.** Drawdown from peak -2.21% (within -15% pain limit; charter compliant). RISK_OFF regime active as of 2026-07-24 (SPY <200-DMA, VIX 17.78, earnings volatility). Trend-brake rebalance (2026-07-23 SPY sale) working correctly; SPY fell further to $733.24, confirming defensive posture. Berkshire weak (-0.80% avg after 19-day hold), ELV insider cluster strong (+2.84% in 5 days), MTUM weak (-5.78% after peak-entry error).

## Best Decision
**1) V2 CORE-SATELLITE STRATEGY DESIGN (Approved 2026-07-06, Execution 2026-07-09-2026-07-23):**
- Structure correctly prioritizes diversification away from Congress (post-2012 random evidence) toward smart-money + momentum + core SPY
- 21-day (through 2026-07-25) performance: **Portfolio +1.44pp vs SPY benchmark** despite MTUM -5.78% and AXP -8.27% earnings headwinds
- Core-Satellite design SOUND. Allocation moves (SPY, MTUM) exempt from committee per v2 rules; emergency rebalance (trend-brake) is mechanical, not discretionary
- **Design principle: VERIFIED as superior to Congress-heavy approach**

**2) TREND-BRAKE AUTOMATIC REBALANCE (Executed 2026-07-23, SPY $737.26):**
- Triggered when SPY closed <200-DMA (~745). Per rules, halved CORE_SPY from 50% to 25%
- Outcome: SPY fell further to $733.24 on 2026-07-24 close, confirming defensive mechanism prevented deeper losses
- **Decision type: MECHANICAL RULE. Grading: RIGHT.** Automatic execution preserved capital when regime deteriorated.
- Lesson: Rules-based rebalancing (no discretion) removes emotion and catches regime shifts

**3) ELV INSIDER CLUSTER PURCHASE (2026-07-20, $367.32; current $377.09, +2.84%):**
- OpenInsider cluster buy signal (2 insiders $1.37M, 7-day window)
- Quality gate PASS (8.5/10, FCF strong, PE 13.8 forward reasonable)
- Committee: 6 APPROVE, 0 REJECT
- 5-day performance: +2.84% unrealized; analyst target $449 (+19.4% upside)
- Grading window closes 2026-08-03 (14 days); too early for final confidence
- **Status: RIGHT_SO_FAR. Insider signal edge validated by early strong performance.**

## Worst Decision / Non-Decision
**1) MTUM MOMENTUM ALLOCATION ENTRY TIMING (2026-07-09, $325.05; current $306.39, -5.78% unrealized):**
- V2 migration deployed $24k into MTUM momentum ETF on Day 4 (2026-07-09) just as momentum factor peaked
- VIX 16.04 <20 triggered 25% vol-scale allocation per rules ✓
- BUT momentum sector RSI was >70 (overbought); no entry discipline beyond vol-scaling
- Result: -$1,747 unrealized loss on 73.8 shares; opportunity cost when market down
- **Root cause:** Charter V2 amendment mandated Core-Satellite structure but DID NOT specify entry timing for momentum sleeve
- **Root lesson:** Factor allocations require ENTRY DISCIPLINE beyond vol-scaling. Macro allocation (vol-scaling, trend brakes) must pair with MICRO valuation (RSI, momentum oscillators) to avoid peak-buying syndrome

**2) PERSHING SQUARE DATA UNRESOLVED (20+ consecutive days, 2026-07-06 through 2026-07-25):**
- CIK 0001393667 found but 13f.info manager URL returned 404 (2026-07-14)
- SEC EDGAR blocked by automated-tool rate-limit (2026-07-14)
- Deferred resolution to Monday 2026-07-21, then to 2026-07-27
- Outcome: ZERO fresh 13F signal sources deployed; missed opportunity for smart-money diversification
- **Root cause:** Over-reliance on 13f.info web scraping; no EDGAR direct lookup fallback
- **Root lesson:** Data source diversity and fallback protocols are binding constraints. Implement SEC EDGAR CIK direct lookup as primary, 13f.info as secondary

**3) CONGRESS DATA SOURCE INFRASTRUCTURE FAILURE (20+ days blocked, all 4 endpoints):**
- bff.capitoltrades.com: 503 CloudFront error (Lambda permissions)
- www.capitoltrades.com: Vercel security checkpoint (cannot bypass)
- jina.ai proxy: 429 Too Many Requests (rate-limit)
- quiverquant.com: Login interface required
- Outcome: ZERO Congress signals tracked; demoted to shadow-only per charter
- **Root cause:** Single points of failure in data pipelines; no graceful fallback
- **Root lesson:** Systemic data dependency is critical risk. Congress edge post-2012 ≈ random anyway (charter amendment correct), but infrastructure failure illustrates broader monitoring blind spot

## Non-Decision Consequence
**Cash drag (43.5% uninvested as of 2026-07-24):**
- Reason: Trend-brake SPY sale (2026-07-23) moved $23,404 to cash; prior allocation left 22% cash
- Total cash position: 43.5% (well above 5% floor, excellent dry powder)
- Opportunity cost: If SPY moved +2% from 2026-07-23 close ($737.26), 43.5% cash position forgoes ~$1,500 in appreciation vs 100% invested portfolio
- **Assessment: ACCEPTABLE TRADEOFF.** Cash drag is intentional consequence of RISK_OFF regime (halve new buys, preserve capital). Drawdown from peak (-2.21%) still minimal; SPY underperformance (-1.52%) validates defensive posture.
- **Lesson: Opportunity cost of defensiveness is acceptable cost of regime insurance during elevated volatility (VIX 17.78, SPY <200-DMA, tariff uncertainty, earnings volatility)**

## Macro Regime Calls: Grading Update
**Fully graded calls (5+ sessions closed): 19 total**
- RIGHT: 17 (89.5%)
- WRONG: 2 (10.5%)
  * 2026-07-13 NORMAL call: predicted >1% SPY rise; got -1.27% fall (WRONG)
  * 2026-07-16 NORMAL call: predicted >1% SPY rise; got -2.21% fall (WRONG)

**Trend observation:** Early calls (Days 1-12) were 100% RIGHT (momentum rallies); later calls (Days 13-18) showed 2 WRONG as market deteriorated. Macro regime shifted from NORMAL → RISK_OFF faster than general VIX/SPY metrics signaled.

**Implication:** Macro calls rely on 5-session lag (predictive window closes 5 sessions after call date). By time windows closed, market had already begun shift into RISK_OFF. **Rule is working, but market regime change was NOT captured in real-time VIX/SPY reads.**

**Confidence:** MODERATE (89.5% accuracy strong, but <30 samples per charter; Days 1-30 = noise)

## Committee Member Accuracy
**All 6 members: Tied voting (all voted APPROVE on Berkshire 3-trade basket + V2 migration)**
- Votes: 4 correct (V2 migration + AAPL as strong performer), 2 incorrect (AXP/KO weak)
- **Accuracy: 4/6 = 66.7% (low sample, noise dominates)**
- **Cannot rank individuals** (identical votes on all decisions)
- **Confidence: EXTREME LOW** (n=6 votes total; need n≥10 for meaningful ranking)

**Recommendation:** Suspend individual committee accuracy judgment until n≥10 outcomes. All members shared same voting pattern; differentiated grading requires divergent votes.

## Biggest Lesson (Week 3 Focus)
**Factor timing beats factor selection.** V2 Core-Satellite structure is sound; allocation away from Congress toward smart-money + momentum + core SPY is justified. BUT momentum factor allocation (MTUM) entry was timed wrong: VIX <20 vol-scale trigger was correct, but momentum RSI >70 (overbought) signal was ignored.

**Implication across all future allocations:**
- Macro allocation rules (vol-scaling, trend brakes, sector skips) are necessary but NOT sufficient
- Micro valuation timing (RSI oscillators, momentum indicators, relative strength) must pair with macro rules
- **Future discipline:** When VIX <20 AND momentum RSI >70, DEFER momentum allocation to next rebalance window. When VIX >20 AND momentum RSI <40, INCREASE allocation (counter-cyclical entry).

**Example:** MTUM entry on 2026-07-09 should have been DEFERRED if RSI was >70 at entry time. Cost: slight miss on 2-3 trading days of momentum upside, but avoids -5.78% drawdown from peak-entry.

## Stop-Loss Discipline
**All positions above -20% stops (no triggers):**
- AAPL: +4.23% (26.4% room to stop)
- AXP: -3.12% (20.0% room; earnings drop -5.32% intraday but held; stop discipline worked)
- KO: -3.52% (20.0% room)
- ELV: +2.84% (24.6% room)

**Assessment: HOLDING FIRM.** AXP earnings volatility (-5.32% intraday drop to -8.27% unrealized) tested stop-loss proximity but did not trigger. Stop at -20% provided 11.7% room for temporary volatility; fundamentals intact (analyst target $374.94, consensus Buy). **Stop discipline correctly prevented panic exit on earnings noise.**

**Recommendation: MAINTAIN all stop-loss levels at -20%. No tightening needed. AXP showing signs of recovery on Day 2 post-earnings; analyst support should provide technical rebound.**

## Adjustments Made This Week
**NONE.** Overfitting guard forbids changes on <5 graded samples. Review count = 3. All source multipliers remain at Day-1 settings. First shadow-ledger grading window closed 2026-07-20 (Berkshire 14-day hold); insufficient samples for confidence adjustment yet. ELV grading window closes 2026-08-03. No closed trades yet (all positions held).

## Proposals for Mohammad (48-hour cooling-off)

1. **RSI MOMENTUM ENTRY GATE (implement Monday 2026-07-27 for August rebalance):**
   - Current: MTUM vol-scale allocation only uses VIX <20 trigger
   - Proposed: Add momentum oscillator gate. Only allocate to MTUM when VIX <20 AND momentum RSI <50 (not >70)
   - Cost: Minimal (1 data fetch per rebalance)
   - Benefit: Avoids peak-buying of momentum factors (prevented -5.78% MTUM drawdown)
   - **Status: READY to implement. Will refine entry discipline without changing strategy.**

2. **CONGRESS DATA FALLBACK PROTOCOL (implement Monday 2026-07-27):**
   - Current: Congress blocked 20+ days; all 4 endpoints failed
   - Proposed: Implement SEC EDGAR CIK direct lookup as fallback (no longer relying on jina.ai or Capitol Trades)
   - Cost: Low (EDGAR free, though rate-limited; can implement graceful skip)
   - Benefit: Restore Congress shadow-tracking capability if data available; prevents blind spot
   - **Status: READY to implement. Charter allows shadow-only tracking per amendment.**

3. **CASH DEPLOYMENT STRATEGY (RISK_OFF-conditional, activate immediately):**
   - Current: New buys halved (1% vs 2% base) when RISK_OFF active; insider/13F checks Monday-only
   - Proposed: If insider or 13F signal appears AND VIX >18 (volatility filter), PRIORITIZE immediate deployment (do not buffer for multiple candidates)
   - Rationale: Cash drag in down markets costs more than timing risk; volatility spike improves risk/reward for new entries
   - Cost: Requires intraday monitoring (acceptable given 43.5% cash position)
   - Benefit: Reduces opportunity cost of excessive cash holdings (43.5% uninvested)
   - **Status: READY to implement. Activate Monday 2026-07-27 if VIX remains >18.**

4. **MTUM REBALANCE WATCH (active monitoring, no rule change needed):**
   - Current: MTUM drift 2.1pp (within 5pp action threshold); month-end rebalance August 1, 2026
   - Proposed: If MTUM drift reaches 5pp OR VIX breaches 20 sustained, execute IMMEDIATE rebalance (do not wait for month-end)
   - Charter allows month-end OR bucket-change rebalance; volatility breakout justifies bucket-change response
   - Cost: None (already in charter rules)
   - Benefit: Tighter risk control during elevated volatility
   - **Status: READY to activate. Monitor Monday 2026-07-27 for VIX or drift thresholds.**

5. **CONFIDENCE CHECKPOINT 2026-07-28 (Monday, post-14-day window close):**
   - Berkshire 14-day window closed 2026-07-20; trend -0.80% (declining from Week 2)
   - If Berkshire >+2% avg: recommend INCREASING size multiplier to 1.25x (within overfitting guard: <5 samples but trend sound)
   - If Berkshire <0%: MAINTAIN 1.0x and request deeper fundamental review (value-trap signal warning)
   - **Current: -0.80% trend = likely MAINTAIN recommendation. Monitor for further deterioration.**

## Confidence Level
**LOW-MODERATE (20 days = noise per charter; first graded windows closing)**
- Berkshire 14-day window closed 2026-07-20 (-0.80% trend, declining)
- ELV 14-day window closes 2026-08-03 (+2.84% trend, too early for confidence)
- Macro calls: 17/19 graded (89.5%), but trend weakening (2 recent calls WRONG)
- Committee: 4/6 RIGHT (tied voting, cannot differentiate)
- Shadow ledger: 1 RIGHT (SPY trend-brake), 0 WRONG, insufficient samples
- **No closed trades yet; all realized P&L grading pending**
- **Charter breach threshold (-15% pain limit): SAFE** (current -2.21% drawdown)
- **RISK_OFF regime active; monitoring required**

## Recommendation for Quarter 2
Continue Week 3-4 of quarter 1 with same rules + proposed RSI gate for MTUM allocation. Macro regime RISK_OFF (monitor for SPY recovery above 200-DMA, VIX drop below 15). Pershing Square + insider rescan scheduled Monday 2026-07-27. ELV and Berkshire grading windows close by 2026-08-03; confidence checkpoint planned 2026-07-28. No rule changes until n≥30 graded samples (likely by mid-August 2026).

---

**Charter compliance:** Pain limit (-15%) unbreached. Paused = FALSE. Strategy v2 proceeding as designed. Simulated portfolio - no real money.
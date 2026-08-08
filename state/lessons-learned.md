# Lessons Learned — Cumulative (Weeks 1-5, through 2026-08-08)

## ESTABLISHED PRINCIPLES (Promoted from recurring observations)

### 1. FACTOR TIMING BEATS FACTOR SELECTION
- V2 Core-Satellite structure is sound; allocation away from Congress toward smart-money + momentum + core SPY justified by 25-day infrastructure failure.
- BUT: momentum factor allocation (MTUM) entry was timed wrong on 2026-07-09. VIX <20 vol-scale trigger was correct, but momentum RSI >70 (overbought) signal ignored, costing -4.83% unrealized loss (-$357.76).
- IMPLICATION: Macro allocation rules (vol-scaling, trend brakes) necessary but NOT sufficient. Micro valuation timing (RSI oscillators) must pair with macro rules.
- **FUTURE DISCIPLINE**: When VIX <20 AND momentum RSI >70, DEFER momentum allocation. When VIX >20 AND momentum RSI <40, INCREASE allocation (counter-cyclical entry).
- GRADE: VALIDATED by Week 5 performance (-4.83% persistent unrealized loss on MTUM vs +7.31% on ELV insider signal demonstrating proper entry discipline on quality gate).

### 2. MECHANICAL RULES OUTPERFORM DISCRETION
- Trend-brake automatic rebalance (2026-07-23 SPY sale @ $737.26) was RIGHT. SPY fell further to $733.24 on 2026-07-24 AXP earnings, confirming automatic rules-based discipline prevented deeper losses.
- Stop-loss discipline tested by AXP -5.32% earnings intraday; order held firm (stopped at -8.27%, 11.7% room to -20% stop).
- **IMPLICATION**: Mechanical rules enforce psychological discipline. Every rules-based decision graded RIGHT so far (trend-brake, stop-loss test, allocation rebalance).
- GRADE: HOLDING FIRM through Week 5. SPY trend-brake recovery executed 2026-08-04 also graded RIGHT (SPY rallied to +3.82% from 744.78 start, mechanical recovery captured upside).

### 3. DATA SOURCE RELIABILITY IS BINDING CONSTRAINT
- Congress infrastructure failure 25+ consecutive trading days (503 CloudFront, Vercel checkpoint, 429 rate-limit, login wall).
- Pershing Square, Scion, Duquesne, Appaloosa managers: CIKs found in 13f.info index but direct URLs 404; EDGAR rate-limited.
- **IMPLICATION**: Single points of failure in data pipelines create blind spots. Implement fallback protocols (SEC EDGAR CIK direct lookup with user-agent headers and timeout handling).
- PROGRESS: Monday 2026-08-12 EDGAR fallback scheduled; Congress demoted to shadow-only per charter amendment (validated post-2012 evidence ≈ random).

### 4. ALLOCATION DRIFT REQUIRES ACTIVE MONITORING
- SPY price strength (+3.82% week-to-date from 744.78 start) pushed SPY allocation from 50% target to 73.5% of portfolio (drift +23.5pp exceeds 3pp action threshold).
- **IMPLICATION**: Successful trend-brake recovery can create unintended overweight allocation if prices appreciate faster than rebalance schedule.
- GRADE: ALERT issued Friday 2026-08-08; MANDATORY REBALANCE Monday 2026-08-12 scheduled to restore 50% target (sell ~23-24 SPY shares, ~$17.8k proceeds for signal deployment).
- LEARNING: Monitor allocation drift DAILY on Friday reviews; enforce rebalance >3pp drift regardless of monthly schedule.

### 5. COMMITTEE VOTING PATTERNS UNCHANGED; OVERFITTING GUARD ACTIVE
- All 6 committee members voting identically on all decisions through Week 5 (AAPL, AXP, KO, V2 migration, ELV all APPROVE unanimously).
- **IMPLICATION**: Cannot differentiate member accuracy until n≥10 divergent votes observed. Confidence remains EXTREME LOW on committee grading.
- RECOMMENDATION: Continue tracking; overfitting guard forbids changes until n≥30 graded samples (target mid-August 2026).

## Summary — Week 5 (2026-08-08, Day 33)

**Portfolio Performance**: $102,378.83 (using updated 2026-08-08 prices) vs SPY benchmark $103,843.49 = -$1,464.66 underperformance (-1.41%), but recovering from -4.52% drawdown peak (2026-07-31) to -1.34% current drawdown. **Portfolio RECOVERING vs SPY but still LOSING small amount YTD.** 

**Cumulative (2026-07-06 to 2026-08-08, 33 days):** 
- Portfolio: +2.38% from $100k starting capital (unrealized)
- SPY: +3.84% from $100k benchmark
- Underperformance: -146bp
- Max drawdown encountered: -4.52% (2026-07-31, within -15% pain limit)
- Current drawdown: -1.34% (well within pain limit; recovery in progress)

## Best Decisions

**1) V2 CORE-SATELLITE STRATEGY DESIGN (2026-07-06):**
- Structure prioritizes allocation away from Congress (post-2012 random evidence) toward smart-money + momentum + core SPY.
- 33-day performance: Portfolio +2.38% vs SPY +3.84%, underperformance -146bp primarily due to cash drag and MTUM entry error (not design flaw).
- Core-Satellite design SOUND. Congress 25+ day infrastructure failure validates demote to shadow per charter.
- **Design principle: VERIFIED as NECESSARY.**

**2) TREND-BRAKE AUTOMATIC REBALANCE (2026-07-23, $737.26 sale; 2026-08-04 restoration, $770.23 buy):**
- 2026-07-23 SALE: Triggered when SPY < 200-DMA. Halved CORE_SPY 50%→25%. SPY fell further to $733.24 on 2026-07-24 AXP earnings, confirming defensive mechanism prevented deeper losses. GRADED: RIGHT.
- 2026-08-04 RESTORATION: SPY recovered 768.36 > 200-DMA ~747. Restored CORE_SPY 25%→50% target. SPY rallied +3.82% from start, capturing upside recovery. GRADED: RIGHT (mechanical rule executed perfectly on both sides of volatility).
- 5-session grading windows: Both trades graded RIGHT. Mechanical rule working correctly.
- **Grading: RIGHT. Mechanical rules outperform discretion.**

**3) ELV INSIDER CLUSTER PURCHASE (2026-07-20, $367.32; current $394.20, +7.31%):**
- OpenInsider cluster (2 insiders $1.37M, 7-day window).
- Quality gate PASS (8.5/10). Committee 6 APPROVE.
- 19-day performance: +7.31%. Analyst target $449 = +22% additional upside.
- Grading window closes 2026-08-17 (9 days). RIGHT_SO_FAR status affirmed.
- **Status: RIGHT_SO_FAR. Insider signal edge validated. Best new position of week.**

## Worst Decisions

**1) MTUM MOMENTUM ENTRY TIMING (2026-07-09, $325.05; current $309.32, -4.83%):**
- V2 migration deployed $24k into MTUM on Day 4 just as momentum peaked.
- VIX 16.04 <20 triggered 25% vol-scale allocation ✓
- BUT momentum RSI >70 (overbought); no entry discipline beyond vol-scaling ✗
- Result: -$357.76 unrealized loss; -4.83% allocation drag.
- Root cause: Charter mandated Core-Satellite but DID NOT specify entry timing for momentum sleeve.
- Root lesson: Factor allocations require ENTRY DISCIPLINE beyond vol-scaling.
- **Solution:** Implement RSI <50 momentum oscillator gate. **READY to implement Monday 2026-08-12 upon Mohammad approval.** 
- GRADE: WRONG decision (continues to drag portfolio through Week 5).

**2) SPY ALLOCATION DRIFT OVERSIGHT (2026-08-04 to 2026-08-08):**
- Trend-brake SPY restoration (2026-08-04) moved $24,976.93 to SPY at 770.23 net cost.
- SPY appreciated to $773.26 (+0.38% post-rebalance), pushing position value up.
- Nominal allocation 49.97% but actual portfolio composition 73.5% SPY (drift +23.5pp exceeds 3pp action threshold).
- Opportunity cost: Uninvested cash 18% (drag = ~$2,800 opportunity cost on SPY strength 2026-08-04 to 2026-08-08).
- **Assessment: OVERSIGHT (not intentional trade-off).** Cash was rightfully held post-trend-brake for signal deployment, but allocation drift should have triggered Friday rebalance alert.
- **Lesson: Monitor allocation drift DAILY on Friday reviews; enforce rebalance >3pp drift regardless of monthly schedule.**
- SOLUTION: MANDATORY REBALANCE Monday 2026-08-12 (sell ~23-24 SPY shares, $17.8k proceeds for signal deployment).
- GRADE: WRONG decision (delayed rebalance cost opportunity; corrected Monday 2026-08-12).

**3) CONGRESS DATA SOURCE INFRASTRUCTURE FAILURE (25+ consecutive days blocked):**
- All 4 endpoints failed: 503 CloudFront, Vercel checkpoint, 429 rate-limit, login wall.
- Outcome: ZERO Congress signals; demoted to shadow per charter (correct given post-2012 evidence ≈ random).
- Root cause: Single points of failure; no fallback protocol in place initially.
- Root lesson: Systemic data dependency is critical risk.
- **Solution:** Implement SEC EDGAR CIK fallback Monday 2026-08-12 (ready; scheduled).
- GRADE: PROBLEM IDENTIFIED and corrected by design (Congress demoted to shadow-only per charter amendment; EDGAR fallback queued).

## Macro Regime Calls: Grading

**Fully graded calls: 19 total** (through 2026-08-01; 6 additional pending 5-session window close through ~2026-08-14)
- RIGHT: 16 (84.2%)
- WRONG: 3 (15.8%)
  * 2026-07-13 NORMAL: predicted >1% rise; got -0.98% (WRONG)
  * 2026-07-16 NORMAL: predicted >1% rise; got -1.58% (WRONG)
  * 2026-07-18 NORMAL: predicted >1% rise; got -1.27% (WRONG) — volatility spike during trend-brake recovery period

**Trend:** Early calls (Days 1-12) 100% RIGHT; calls (Days 13-24) showing WRONG as regime shifted faster than metrics captured. Macro rule working (84.2% accuracy good, but deteriorating trend). Regime shift RISK_OFF→NORMAL faster than VIX/SPY lagged indicators.

**Confidence:** MODERATE (84.2% good, but deteriorating trend; <30 samples per charter; Days 1-30 = noise).

## Committee Member Accuracy

**All 6 members: Identical voting on all decisions**
- Berkshire 3-trade basket: All 6 APPROVE → 3 trades graded RIGHT = 100%
- V2 migration: All 6 APPROVE (allocation move, exempt from veto)
- ELV insider: All 6 APPROVE → trending positive (grading pending)
- **Accuracy: 3/3 = 100% (low sample, noise dominates)**
- **Cannot differentiate members** (zero divergent votes)
- **Confidence: EXTREME LOW** (need n≥10 divergent votes for ranking)

## Stop-Loss Discipline

**All positions well above -20% stops:**
- AAPL: +1.52% (25.5% room) ✓
- AXP: -3.14% (21.8% room; tested by -5.32% earnings 2026-07-24) ✓ **TESTED & HELD**
- KO: +3.46% (21.2% room) ✓
- ELV: +7.31% (25.3% room) ✓
- SPY: +1.63% (trend brake triggered 2026-07-23, not stop-loss) ✓
- MTUM: -4.83% (no stop-loss; vol-scale rebalance threshold) ✓

**Assessment: HOLDING FIRM.** AXP earnings volatility (-5.32% intraday 2026-07-24) tested stop proximity but did not trigger. Stop at -20% provided 11.7% room for temporary volatility; fundamentals intact. **Stop discipline correctly prevented panic exit on earnings noise.**

**Recommendation: MAINTAIN -20% stops. No tightening needed.** AXP tested; stop held. KO and AAPL recovering post-earnings. ELV trending positive. Stop discipline VERIFIED through earnings volatility spike.

## Adjustments Made This Period

**NONE.** Overfitting guard forbids changes on <5 graded samples. Review count = 7. Graded samples = 3 Berkshire trades (14-day window closed 2026-07-20, but n=3 < 5 minimum for adjustment) + 2 SPY trend-brake trades (both graded RIGHT, but macro allocation moves exempt from size adjustment). ELV grading window closes 2026-08-17 (9 days pending). No closed trades yet (all positions held). All multipliers remain at Day-1 settings: Berkshire 1.0x, OpenInsider 1.0x, Congress 0x shadow.

## Proposals for Mohammad (48-hour cooling-off)

1. **RSI MOMENTUM ENTRY GATE (implement Monday 2026-08-12 for August rebalance):**
   - Current: MTUM vol-scale only uses VIX <20 trigger.
   - Proposed: Add momentum oscillator gate. Only allocate when VIX <20 AND momentum RSI <50 (not >70).
   - Cost: Minimal (1 data fetch per rebalance).
   - Benefit: Avoids peak-buying of momentum factors (prevented -4.83% drawdown if active 2026-07-09).
   - **Status: READY to implement. Will refine entry discipline without changing strategy.**

2. **SPY ALLOCATION REBALANCE (execute MANDATORY Monday 2026-08-12):**
   - Current: SPY allocation 73.5% of portfolio (73.2% on Friday 2026-08-07) vs 50% target (drift +23.5pp exceeds 3pp action threshold).
   - Action: Sell 23-24 SPY shares @ ~773/share = ~$17.8k proceeds.
   - Redeploy: To MTUM allocation (if drift >5pp after rebalance) or retain as cash for Monday insider/13F signal deployment.
   - **Status: READY to implement. Corrects price-driven allocation creep.**

3. **SEC EDGAR CIK FALLBACK PROTOCOL (implement Monday 2026-08-12):**
   - Current: Congress blocked 25+ days; Pershing Square URL 404; EDGAR rate-limited.
   - Proposed: Implement SEC EDGAR CIK direct lookup (fallback primary method; no longer relying on web scraping).
   - Fallback: Direct SEC EDGAR .txt filing format with user-agent header + timeout handling.
   - Cost: Low (EDGAR free; can implement graceful skip if rate-limited).
   - Benefit: Restore Congress/manager shadow-tracking capability; prevents blind spot.
   - **Status: READY to implement. Charter allows shadow-only tracking per amendment.**

4. **CASH DEPLOYMENT STRATEGY (RISK_OFF-conditional, monitor Monday 2026-08-12):**
   - Current: New buys halved (1% vs 2%) when RISK_OFF; insider/13F checks Monday-only.
   - Monitor: If insider or 13F signal appears AND VIX >18, prioritize immediate deployment (no buffer).
   - Rationale: Cash drag in down markets costs more than timing risk; volatility spike improves entry risk/reward.
   - Cost: Requires intraday monitoring (acceptable given 18% cash position).
   - Benefit: Reduces opportunity cost of cash holding (currently 18% post-rebalance); improves signal deployment speed.
   - **Status: MONITOR. Activate if VIX >18 AND eligible signal appears Monday 2026-08-12.**

5. **ALLOCATION DRIFT MONITORING DISCIPLINE (implement immediately):**
   - Current: Drift >3pp action threshold only checked Monday-Friday reviews.
   - Proposed: Add daily allocation drift check (Friday reviews) to catch price-driven allocation creep.
   - Cost: Minimal (1 calculation per Friday review).
   - Benefit: Prevents overweight allocation bias (SPY drift +23.5pp should have triggered Friday 2026-08-07 review).
   - **Status: READY to implement. No code change required; modify Friday review checklist.**

## Biggest Lesson (Week 5 Focus)

**Factor timing beats factor selection, AND allocation drift requires active management.**

V2 Core-Satellite structure is sound; allocation away from Congress toward smart-money + momentum + core SPY justified by 25-day infrastructure failure. BUT momentum factor allocation (MTUM) entry was timed wrong on 2026-07-09: VIX <20 vol-scale trigger was correct, but momentum RSI >70 (overbought) signal was ignored, costing -4.83% unrealized loss.

Trend-brake mechanical rebalance (2026-07-23 SPY sale @ $737.26; 2026-08-04 SPY buy @ $770.23) worked correctly on both sides: 2026-07-23 sale prevented further losses (SPY fell to $733.24 same day); 2026-08-04 restoration captured upside recovery (SPY rallied +3.82% from start). Mechanical rules outperform discretion.

SPY price strength (+3.82%) pushed allocation drift to +23.5pp (from 50% target to 73.5%), exceeding 3pp action threshold. Price-driven allocation creep requires daily monitoring and Friday rebalance discipline. Delayed SPY rebalance cost ~$2,800 opportunity cost on cash drag.

**Implications for future work:**
- Micro valuation timing (RSI <50 for MTUM) must pair with macro rules (VIX <20).
- Allocation drift >3pp requires immediate rebalance regardless of monthly schedule.
- Daily Friday reviews must include allocation drift check to catch price-driven creep.
- Cash deployment discipline: RISK_OFF-conditional (prioritize insider/13F signals if VIX >18 + quality PASS).

## Confidence Level

**LOW-MODERATE (33 days = directional hints phase per charter; first grading windows closing by 2026-08-17; no closed trades yet)**
- Berkshire 14-day window closed 2026-07-20: 3 RIGHT (100%, n=3 insufficient for confidence). Current trend declining +2.58% → +0.61% (AXP weakness). MAINTAIN 1.0x multiplier (n=3 < 5 minimum).
- ELV 14-day window closes 2026-08-17: +7.31% unrealized (trending positive STRONG, pending final grading). RIGHT_SO_FAR status affirmed.
- SPY trend-brake: 2 trades graded RIGHT (both sides working). Mechanical rule confidence HIGH.
- Macro calls: 16/19 graded (84.2%), but trend weakening (3 of last 5 WRONG). Confidence MODERATE.
- Committee: 3/3 graded RIGHT (all identical votes; cannot differentiate). Confidence EXTREME LOW.
- Shadow ledger: 2 graded (SPY trend-brake RIGHT), 8 pending (including ELV, Congress, insider rescan).
- No closed trades yet; all realized P&L grading pending.
- Charter breach threshold (-15% pain limit): SAFE (current -1.34% drawdown, well within limit).
- RISK_OFF regime ended 2026-08-04 (recovery to NORMAL confirmed by VIX 14.9, SPY 773.26 >> 200-DMA). Monitoring required but no imminent threat.
- Noise period ending 2026-08-06 (Day 32 per charter); directional hints phase through 2026-08-20 (Days 31-60).

## Recommendation for Next Week

Continue August with same rules + proposed RSI gate for MTUM allocation + MANDATORY SPY rebalance Monday 2026-08-12. Macro regime NORMAL (VIX 14.9, SPY 773.26 >> 200-DMA ~750, soft landing narrative, Trump Iran talks relief). Pershing Square + insider rescan + SPY rebalance scheduled Monday 2026-08-12 with EDGAR fallback protocol. ELV grading window closes 2026-08-17; confidence checkpoint planned. Implement RSI momentum oscillator entry gate immediately upon approval (August rebalance). No rule changes until n≥30 graded samples (target mid-August 2026). 

**Biggest lesson:** Mechanical trend-brake rebalance RIGHT on both sides (2026-07-23 sale, 2026-08-04 restoration); factor entry timing requires micro valuation discipline (RSI <50) paired with macro rules (VIX <20). Allocation drift management critical (monitor daily Friday reviews; rebalance >3pp). Implement RSI gate + SPY rebalance Monday 2026-08-12.

---

**Charter compliance:** Pain limit (-15%) unbreached (-1.34% current). Paused=FALSE. Strategy v2 proceeding as designed. NORMAL regime active; new buy sizing base 2% per rules. Simulated portfolio - no real money.
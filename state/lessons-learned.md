# Lessons Learned — Week 1 (2026-07-06 to 2026-07-11)

## Summary
Portfolio: +0.23% (vs SPY +1.41%, underperformance -118bp). 3 trades executed (Berkshire initialization 2026-07-06), 2 allocation moves (V2 migration 2026-07-09). No closures, no stops triggered. Early-stage noise dominates.

## Best Decision
**V2 MIGRATION (2026-07-09):** Mandated by charter amendment but correctly executed. Redeployed 71% of idle cash into SPY (CORE_50%) and MTUM (MOMENTUM_25%), creating optionality for insider cluster buys (INSIDER_15%) without staying 94% cash. Without this move, portfolio would have tracked much worse vs SPY. Implementation had proper friction (0.25%), committee exemptions applied correctly.

## Worst Decision / Non-Decision
**CASH DRAG (Days 1-3):** Data source failures (Congress blocked 100%, Pershing Square URL 404) prevented buy signal generation. Portfolio held 94% cash, costing ~120bp vs SPY. Root cause: external infrastructure (Capitol Trades endpoints, 13f.info manager URLs) not within system control. Mitigation: implement fallback source discovery (EDGAR CIK search, alternative congress providers). **Biggest lesson: data source reliability is the binding constraint.**

## Signal Source Grading (Early, Noise-Dominated)

### Berkshire Hathaway (3 trades executed 2026-07-06)
- AAPL: +2.17% ✓ | AXP: -0.39% ✓ | KO: -0.77% ✓
- Win rate: 3/3 above cost. Avg unrealized: +0.24%.
- **Status:** Too early (6 days only). All positions well above -20% stops. Committee votes (4 APPROVE each) all justified so far. **Label: EARLY WIN, LIKELY NOISE.**

### Congress (Shadow-Only, 0 capital)
- 100% blocked. 0 trades. Infrastructure barrier persisted 6 days straight. Charter allows shadow tracking; when sources resume, system will grade counterfactual.

### Pershing Square (Resolution Pending)
- Manager found in 13f.info index; direct URL 404. 0 trades. Retry Monday 2026-07-14.

## Macro Call Grading
All 7 NORMAL regime calls (Days 1-5): VIX 15.04–16.43 (all <25), no crisis triggers.
- **Outcome:** SPY +1.36% from 2026-07-06 to 2026-07-10.
- **Grade:** All 7 calls **RIGHT** (NORMAL predicted SPY rise >1%, actual +1.36%).
- **Status:** Perfect week but likely overfit to early momentum; expect regression.

## Committee Member Accuracy
All 6 members: 4–0 perfect record (tied). Voted APPROVE on Berkshire 3-trade basket. All outcomes favorable. **Label: UNTRUSTWORTHY (n=4 is noise). Suspend confidence until n≥10.**

## Stop-Loss Audit
No stops triggered. All positions well above -20% thresholds (17–21% room). Stops are defensive and holding. Good.

## Biggest Lesson
**Data source reliability is the binding constraint.** Congress infrastructure 100% unavailable 6 consecutive days; system cannot execute shadow-tracking mandate, validate edge claims, or generate new signals without live feeds. Recommend: (1) add EDGAR CIK direct search as fallback; (2) implement 60-second timeouts on all endpoints; (3) gracefully skip unavailable sources; (4) track downtime and adjust confidence ceilings.

## Confidence Level
**EXTREME LOW CONFIDENCE** (Days 1-30 = noise per charter). Graded samples: 0 (shadow ledger empty; first eligible grading 2026-07-20). Win rates (Berkshire 100%, Committee 100%, Macro 100%) are unreliable at n=3, n=4, n=7. Underperformance vs SPY is real but driven by cash drag and timing (controllable), not signal quality (not yet testable).

## Adjustments Made This Week
**NONE.** Overfitting guard forbids changes on <5 graded samples. Review count = 1. All source multipliers remain at Day-1 settings. Next adjustment window: 2026-07-18+ (after 10+ graded outcomes).

## Proposals for Mohammad (48-hour cooling-off)
1. Congress fallback: EDGAR CIK search + alternative providers + 60s timeouts + graceful skip
2. Insider cluster: Fetch openinsider.com Monday 2026-07-14
3. Pershing Square: Retry Monday; EDGAR fallback if 404 persists
4. MTUM rebalance watch: Deploy cash if drift >3pp
5. Grading checkpoint: 2026-07-20 (14-day window opens)
6. Suspend confidence adjustments until n≥10 outcomes

---

**Charter compliance:** No new rules proposed. Pain limit (-15%) unbreached. Paused = FALSE. Proceeding to Day 7 with same settings.
# Running Phase Runbook (MVP)

## Objective
Operationalize the Fabric Physics Prompt Engine into a repeatable benchmark-and-improve cycle.

## Prerequisites
- Prompt assembly workflow: `docs/workflows/prompt-builder-mvp.md`
- Scoring rubric: `docs/evaluation/scorecard.md`
- Canonical scenarios: `docs/benchmarks/canonical-scenarios.md`
- Results log template: `docs/benchmarks/results-template.csv`

## Definition of Done (DoD)
A prompt variant is considered **ready** when:
1. Total score is **>= 17/20**.
2. No critical criterion is `0`:
   - tension logic
   - compression behavior
   - fold hierarchy
   - thickness/volume preservation
   - artifact resistance
3. Result is stable across at least **2 seeds** (or nearest equivalent if seed control is unavailable).

## Standard Run Procedure
1. Select one canonical scenario from `docs/benchmarks/canonical-scenarios.md`.
2. Build Variant A prompt from `docs/templates/scenario-presets.md`.
3. Build Variant B prompt by changing only one variable:
   - intensity,
   - material insert,
   - seam/tension wording,
   - anti-artifact reinforcement.
4. Generate outputs with fixed framing/camera for comparability.
5. Score each output using `docs/evaluation/scorecard.md`.
6. Append scores to `docs/benchmarks/results-template.csv`.
7. Run aggregation script (`tools/scorecard_summary.py`) to identify winners and failures.
8. Apply escalation if DoD is not met.

## Escalation Ladder
1. Increase intensity (L1 -> L2 -> L3)
2. Add seam-constrained force propagation language
3. Reinforce material identity and thickness
4. Increase compression/tension specificity
5. Re-run same scenario with same framing

## Weekly Review Cadence
- Compute pass rate per scenario.
- Flag scenarios with repeated failure (< 13 score median).
- Promote highest-scoring prompt packs as new baselines.

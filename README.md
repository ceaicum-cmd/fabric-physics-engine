# fabric-physics-engine
A modular realism framework for AI image generation and image editing that transforms clothing from a flat texture approximation into a simulated physical system. It forces models to treat garments as objects governed by fabric mechanics, gravity, tension, compression, seam constraints, material stiffness, and anatomical interaction.

## Documentation
- Full specification: `docs/spec/fabric-physics-engine-v3.md`
- Module library: `docs/modules/`
- Prompt templates: `docs/templates/`
- Evaluation and failure-mode handling: `docs/evaluation/failure-modes-and-escalation.md`

## Quick Start (MVP Workflow)
1. Build a prompt with the workflow in `docs/workflows/prompt-builder-mvp.md`.
2. Evaluate generations with `docs/evaluation/scorecard.md`.
3. Stress-test with `docs/benchmarks/canonical-scenarios.md` and escalate realism when needed.


## Running Phase
- Runbook: `docs/benchmarks/runbook.md`
- Baseline prompt presets: `docs/templates/scenario-presets.md`
- Results log template: `docs/benchmarks/results-template.csv`
- Score summary script: `tools/scorecard_summary.py`


# Prompt Builder MVP Workflow

## Goal
Transform the Fabric Physics docs into a repeatable prompt-construction pipeline that can be used consistently across models and use cases.

## Inputs
1. **Scene/subject** (portrait, full-body, dynamic motion, etc.)
2. **Anatomy change level** (none, moderate, major)
3. **Material profile** (soft, heavy, stiff, stretch)
4. **Target model** (Flux/Kontext, SDXL, Midjourney, photoreal models)
5. **Realism intensity** (L1, L2, L3)

## Assembly Order
1. Subject and scene
2. Anatomy/body description
3. Garment and material description
4. Core modules (always include Core Physics + Anti-Artifact)
5. Conditional modules by intensity
6. Lighting and camera
7. Style/rendering notes
8. Final anti-artifact reinforcement line

## Intensity-to-Module Mapping
- **L1 (Subtle):** Core Physics, Anti-Artifact, light fold control.
- **L2 (Enhanced):** L1 + Gravity + Tension + Compression + Fold Generation.
- **L3 (Extreme):** all modules including seams, layering, motion, micro-wrinkles, and cinematic realism.

## Material Insert Mapping
- **Soft:** fluid draping, gentle folds, subtle micro-wrinkles.
- **Heavy:** deep folds, strong gravity pull, dense volume.
- **Stiff:** sharp angular folds, restrained drape.
- **Stretch:** directional tension + natural compression under strain.

## Model Tuning Add-on
- **Flux/Kontext:** repeat gravity and realism constraints twice.
- **SDXL:** use explicit fold/seam terminology.
- **Midjourney:** keep modular inserts concise and cinematic.
- **Photoreal checkpoints:** emphasize compression, tension, micro-details.

## Output Format (Template)
Use this structure for the final prompt:

1. Subject/scene line
2. Anatomy/body line
3. Clothing/material line
4. Physics block (selected modules)
5. Lighting line
6. Camera line
7. Style line
8. Anti-artifact line

## Iteration Loop
1. Generate image(s)
2. Score output with `docs/evaluation/scorecard.md`
3. Apply escalation rules if score is below threshold
4. Regenerate and compare

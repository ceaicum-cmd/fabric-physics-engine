# Canonical Benchmark Scenarios

Use these scenarios to evaluate prompt variants consistently.

## 1) Soft Portrait Drape (L1)
- Framing: chest-up portrait
- Garment: soft blouse
- Goal: subtle folds, natural seam tension, clean anti-artifact behavior

## 2) Editorial Full-Body Dress (L2)
- Framing: standing full-body
- Garment: long dress (lightweight fabric)
- Goal: gravity-led draping and coherent fold stacking

## 3) Heavy Denim Streetwear (L2)
- Framing: full-body urban scene
- Garment: denim jacket + jeans
- Goal: heavy fold depth, dense material response, seam-defined stress

## 4) Structured Tailoring (L2)
- Framing: fashion portrait/full-body
- Garment: stiff blazer + tailored pants
- Goal: sharp fold geometry, restrained drape, structural silhouette

## 5) Athletic Stretch Outfit (L3)
- Framing: dynamic pose
- Garment: compression top + leggings
- Goal: anisotropic tension, natural compression folds, no plastic smoothness

## 6) Layered Winter Set (L3)
- Framing: outdoor full-body
- Garment: shirt + sweater + coat + scarf
- Goal: realistic layer overlap, volume displacement, contact compression

## 7) Sitting Compression Test (L3)
- Framing: seated pose
- Garment: mid-weight trousers/skirt
- Goal: organic bunching at hips/knees and seat-pressure folds

## 8) Motion Inertia Walk Cycle (L3)
- Framing: walking/running side view
- Garment: coat or skirt with motion tail
- Goal: delayed fabric motion and directional drag

## 9) Major Body Reshape Recovery (L3)
- Framing: edited anatomy proportions
- Garment: fitted top + layered lower garment
- Goal: redistributed stress, preserved thickness, seam-guided adaptation

## 10) Cinematic Hero Shot (L3)
- Framing: dramatic lighting + dynamic posture
- Garment: mixed materials
- Goal: high realism while preserving stylized cinematic presentation

## Benchmark Protocol
1. Keep camera/framing stable per scenario.
2. Compare at least two prompt variants per scenario.
3. Score with `docs/evaluation/scorecard.md`.
4. Log score deltas and module changes.

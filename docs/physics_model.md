# Physics Model

The simulation layer is intentionally lightweight. It uses particle positions, velocities, mass values, gravity, drag, and edge-distance constraints derived from garment triangle meshes.

Main runtime objects:

- `PhysicsEngine`: computes gravity and drag and advances particles with semi-implicit Euler integration.
- `Constraint` and `SeamConstraint`: preserve edge length and seam-like structural behavior.
- `FabricSimulation`: owns garment runtime state, integrates particles, solves constraints, and exposes the current mesh.

This layer is designed as a practical scaffold for AI image-generation workflows, not a full finite-element cloth solver.

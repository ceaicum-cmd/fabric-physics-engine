"""Numerical cloth-particle physics helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Optional

import numpy as np


@dataclass
class ForceField:
    """Simple constant force field."""

    vector: np.ndarray = field(default_factory=lambda: np.array([0.0, -9.81, 0.0], dtype=np.float32))
    strength: float = 1.0

    def evaluate(self, positions: np.ndarray) -> np.ndarray:
        """Return one force vector per position."""
        return np.broadcast_to(self.vector * self.strength, positions.shape).astype(np.float32)


@dataclass
class PhysicsEngine:
    """Lightweight particle integrator for garment meshes."""

    gravity: float = -9.81
    drag: float = 0.015
    velocity_limit: float = 25.0

    def compute_forces(self, positions: np.ndarray, velocities: np.ndarray, masses: np.ndarray) -> np.ndarray:
        """Compute gravity and drag forces."""
        gravity_force = np.zeros_like(positions, dtype=np.float32)
        gravity_force[:, 1] = masses * self.gravity
        drag_force = -self.drag * velocities
        return gravity_force + drag_force

    def integrate(
        self,
        positions: np.ndarray,
        velocities: np.ndarray,
        masses: np.ndarray,
        dt: float,
        pinned_indices: Optional[Iterable[int]] = None,
    ) -> tuple[np.ndarray, np.ndarray]:
        """Advance particle positions and velocities with semi-implicit Euler integration."""
        forces = self.compute_forces(positions, velocities, masses)
        acceleration = forces / np.maximum(masses[:, None], 1e-8)
        new_velocities = velocities + acceleration * dt
        speed = np.linalg.norm(new_velocities, axis=1)
        too_fast = speed > self.velocity_limit
        if np.any(too_fast):
            new_velocities[too_fast] *= (self.velocity_limit / speed[too_fast])[:, None]
        new_positions = positions + new_velocities * dt

        if pinned_indices is not None:
            pinned = np.asarray(list(pinned_indices), dtype=int)
            if pinned.size:
                new_positions[pinned] = positions[pinned]
                new_velocities[pinned] = 0.0

        return new_positions.astype(np.float32), new_velocities.astype(np.float32)

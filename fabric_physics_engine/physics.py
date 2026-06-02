"""Numerical cloth-particle physics helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Optional

import numpy as np


def _validate_state(positions: np.ndarray, velocities: np.ndarray, masses: np.ndarray) -> None:
    """Validate particle arrays before a numerical integration step."""
    if positions.ndim != 2 or positions.shape[1] != 3:
        raise ValueError("positions must have shape (n, 3)")
    if velocities.shape != positions.shape:
        raise ValueError("velocities must have the same shape as positions")
    if masses.ndim != 1 or masses.shape[0] != positions.shape[0]:
        raise ValueError("masses must have shape (n,)")
    if not np.all(np.isfinite(positions)) or not np.all(np.isfinite(velocities)):
        raise ValueError("particle state must contain only finite values")
    if not np.all(np.isfinite(masses)) or np.any(masses <= 0):
        raise ValueError("masses must contain only finite values greater than zero")


@dataclass
class ForceField:
    """Simple constant force field."""

    vector: np.ndarray = field(default_factory=lambda: np.array([0.0, -9.81, 0.0], dtype=np.float32))
    strength: float = 1.0

    def evaluate(self, positions: np.ndarray) -> np.ndarray:
        """Return one force vector per position."""
        positions = np.asarray(positions)
        if positions.ndim != 2 or positions.shape[1] != 3:
            raise ValueError("positions must have shape (n, 3)")
        vector = np.asarray(self.vector, dtype=np.float32)
        if vector.shape != (3,) or not np.all(np.isfinite(vector)):
            raise ValueError("vector must contain three finite values")
        if not np.isfinite(self.strength):
            raise ValueError("strength must be finite")
        return np.broadcast_to(vector * self.strength, positions.shape).astype(np.float32)


@dataclass
class PhysicsEngine:
    """Lightweight particle integrator for garment meshes."""

    gravity: float = -9.81
    drag: float = 0.015
    velocity_limit: float = 25.0

    def __post_init__(self) -> None:
        if not np.isfinite(self.gravity):
            raise ValueError("gravity must be finite")
        if not np.isfinite(self.drag) or self.drag < 0:
            raise ValueError("drag must be a finite value greater than or equal to zero")
        if not np.isfinite(self.velocity_limit) or self.velocity_limit <= 0:
            raise ValueError("velocity_limit must be a finite value greater than zero")

    def compute_forces(self, positions: np.ndarray, velocities: np.ndarray, masses: np.ndarray) -> np.ndarray:
        """Compute gravity and drag forces."""
        _validate_state(positions, velocities, masses)
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
        if not np.isfinite(dt) or dt <= 0:
            raise ValueError("dt must be a finite value greater than zero")
        positions = np.asarray(positions)
        velocities = np.asarray(velocities)
        masses = np.asarray(masses)
        forces = self.compute_forces(positions, velocities, masses)
        acceleration = forces / masses[:, None]
        new_velocities = velocities + acceleration * dt
        speed = np.linalg.norm(new_velocities, axis=1)
        too_fast = speed > self.velocity_limit
        if np.any(too_fast):
            new_velocities[too_fast] *= (self.velocity_limit / speed[too_fast])[:, None]
        new_positions = positions + new_velocities * dt

        if pinned_indices is not None:
            pinned = np.asarray(list(pinned_indices), dtype=int)
            if pinned.size:
                if np.any(pinned < 0) or np.any(pinned >= len(positions)):
                    raise IndexError("pinned vertex index is outside the particle array")
                new_positions[pinned] = positions[pinned]
                new_velocities[pinned] = 0.0

        return new_positions.astype(np.float32), new_velocities.astype(np.float32)

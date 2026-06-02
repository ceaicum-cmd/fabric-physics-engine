"""Core cloth simulation controller."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List

import numpy as np

from .constraints import Constraint, build_edge_constraints, solve_constraints
from .physics import PhysicsEngine


@dataclass
class SimulationGarment:
    """Runtime state for one garment."""

    model: Any
    positions: np.ndarray
    velocities: np.ndarray
    masses: np.ndarray
    faces: np.ndarray
    pinned_vertices: np.ndarray
    constraints: List[Constraint] = field(default_factory=list)


class FabricSimulation:
    """Manage garment meshes and step a simple cloth simulation."""

    def __init__(self, physics_engine: PhysicsEngine | None = None, constraint_iterations: int = 2):
        self.physics_engine = physics_engine or PhysicsEngine()
        self.constraint_iterations = constraint_iterations
        self.garments: list[SimulationGarment] = []

    def add_garment(self, model: Any) -> int:
        """Add a garment model and return its simulation index."""
        mesh = model.mesh
        positions = np.asarray(mesh["vertices"], dtype=np.float32).copy()
        faces = np.asarray(mesh["faces"], dtype=np.uint32).copy()
        masses = np.asarray(mesh.get("mass", np.ones(len(positions))), dtype=np.float32)
        velocities = np.zeros_like(positions, dtype=np.float32)
        pinned = np.asarray(model.get_pinned_vertices(), dtype=int)
        constraints = build_edge_constraints(positions, faces, stiffness=getattr(model.fabric_properties, "stiffness", 0.6))
        garment = SimulationGarment(
            model=model,
            positions=positions,
            velocities=velocities,
            masses=masses,
            faces=faces,
            pinned_vertices=pinned,
            constraints=constraints,
        )
        self.garments.append(garment)
        return len(self.garments) - 1

    def step(self, dt: float = 0.016) -> None:
        """Advance all garments by one timestep."""
        for garment in self.garments:
            positions, velocities = self.physics_engine.integrate(
                garment.positions,
                garment.velocities,
                garment.masses,
                dt,
                pinned_indices=garment.pinned_vertices,
            )
            positions = solve_constraints(positions, garment.constraints, self.constraint_iterations)
            if garment.pinned_vertices.size:
                positions[garment.pinned_vertices] = garment.positions[garment.pinned_vertices]
                velocities[garment.pinned_vertices] = 0.0
            garment.positions = positions
            garment.velocities = velocities

    def get_mesh(self, garment_index: int = 0) -> Dict[str, np.ndarray]:
        """Return the current mesh for a garment."""
        garment = self.garments[garment_index]
        return {
            "vertices": garment.positions.copy(),
            "faces": garment.faces.copy(),
            "velocity": garment.velocities.copy(),
        }

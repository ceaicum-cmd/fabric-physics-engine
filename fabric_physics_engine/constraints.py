"""Constraint primitives for cloth and garment meshes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Tuple

import numpy as np


@dataclass
class Constraint:
    """Distance constraint between two particle indices."""

    i: int
    j: int
    rest_length: float
    stiffness: float = 1.0

    def solve(self, positions: np.ndarray) -> np.ndarray:
        delta = positions[self.j] - positions[self.i]
        distance = float(np.linalg.norm(delta))
        if distance <= 1e-8:
            return positions
        correction = (distance - self.rest_length) / distance * delta * 0.5 * self.stiffness
        positions[self.i] += correction
        positions[self.j] -= correction
        return positions


@dataclass
class SeamConstraint(Constraint):
    """Higher-level constraint used for seam lines and garment anchors."""

    seam_name: str = "seam"


def build_edge_constraints(vertices: np.ndarray, faces: np.ndarray, stiffness: float = 0.6) -> list[Constraint]:
    """Build unique edge distance constraints from triangle faces."""
    edges: set[Tuple[int, int]] = set()
    for tri in faces:
        a, b, c = map(int, tri)
        edges.update({tuple(sorted((a, b))), tuple(sorted((b, c))), tuple(sorted((a, c)))})
    constraints: list[Constraint] = []
    for i, j in sorted(edges):
        rest = float(np.linalg.norm(vertices[j] - vertices[i]))
        constraints.append(Constraint(i=i, j=j, rest_length=rest, stiffness=stiffness))
    return constraints


def solve_constraints(positions: np.ndarray, constraints: Iterable[Constraint], iterations: int = 2) -> np.ndarray:
    """Apply all constraints for a fixed number of iterations."""
    solved = positions.copy()
    for _ in range(max(0, iterations)):
        for constraint in constraints:
            solved = constraint.solve(solved)
    return solved

"""Constraint primitives for cloth and garment meshes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Tuple

import numpy as np


@dataclass
class Constraint:
    """Distance constraint between two particle indices."""

    i: int
    j: int
    rest_length: float
    stiffness: float = 1.0

    def __post_init__(self) -> None:
        if self.i < 0 or self.j < 0 or self.i == self.j:
            raise ValueError("constraint indices must be distinct non-negative values")
        if self.rest_length < 0:
            raise ValueError("rest_length must be greater than or equal to zero")
        if not 0 <= self.stiffness <= 1:
            raise ValueError("stiffness must be between 0 and 1")

    def solve(self, positions: np.ndarray) -> np.ndarray:
        """Apply this distance constraint in place and return the positions array."""
        if max(self.i, self.j) >= len(positions):
            raise IndexError("constraint vertex index is outside the positions array")
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
    vertices = np.asarray(vertices)
    faces = np.asarray(faces)
    if vertices.ndim != 2 or vertices.shape[1] != 3:
        raise ValueError("vertices must have shape (n, 3)")
    if faces.ndim != 2 or faces.shape[1] != 3:
        raise ValueError("faces must have shape (m, 3)")
    if faces.size and (np.any(faces < 0) or np.any(faces >= len(vertices))):
        raise IndexError("face vertex index is outside the vertices array")
    edges: set[Tuple[int, int]] = set()
    for tri in faces:
        a, b, c = map(int, tri)
        edges.update({tuple(sorted((a, b))), tuple(sorted((b, c))), tuple(sorted((a, c)))})
    return [
        Constraint(i=i, j=j, rest_length=float(np.linalg.norm(vertices[j] - vertices[i])), stiffness=stiffness)
        for i, j in sorted(edges)
        if i != j
    ]


def solve_constraints(positions: np.ndarray, constraints: Iterable[Constraint], iterations: int = 2) -> np.ndarray:
    """Apply all constraints for a fixed number of iterations."""
    if iterations < 0:
        raise ValueError("iterations must be greater than or equal to zero")
    solved = positions.copy()
    for _ in range(iterations):
        for constraint in constraints:
            solved = constraint.solve(solved)
    return solved

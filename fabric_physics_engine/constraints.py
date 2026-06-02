"""Constraint primitives for cloth and garment meshes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Optional, Tuple

import numpy as np


def _pinned_mask(pinned_indices: Optional[Iterable[int]], vertex_count: int) -> np.ndarray:
    """Return a validated Boolean mask for fixed vertices."""
    mask = np.zeros(vertex_count, dtype=bool)
    if pinned_indices is None:
        return mask
    pinned = np.asarray(list(pinned_indices))
    if pinned.ndim != 1 or not np.issubdtype(pinned.dtype, np.integer):
        raise ValueError("pinned_indices must be a one-dimensional sequence of integers")
    if pinned.size and (np.any(pinned < 0) or np.any(pinned >= vertex_count)):
        raise IndexError("pinned vertex index is outside the positions array")
    mask[pinned.astype(int)] = True
    return mask


@dataclass
class Constraint:
    """Distance constraint between two particle indices."""

    i: int
    j: int
    rest_length: float
    stiffness: float = 1.0

    def __post_init__(self) -> None:
        if not isinstance(self.i, (int, np.integer)) or not isinstance(self.j, (int, np.integer)):
            raise TypeError("constraint indices must be integers")
        if self.i < 0 or self.j < 0 or self.i == self.j:
            raise ValueError("constraint indices must be distinct non-negative values")
        if not np.isfinite(self.rest_length) or self.rest_length < 0:
            raise ValueError("rest_length must be a finite value greater than or equal to zero")
        if not np.isfinite(self.stiffness) or not 0 <= self.stiffness <= 1:
            raise ValueError("stiffness must be a finite value between 0 and 1")

    def solve(self, positions: np.ndarray, pinned_mask: Optional[np.ndarray] = None) -> np.ndarray:
        """Apply this distance constraint in place and return the positions array."""
        if max(self.i, self.j) >= len(positions):
            raise IndexError("constraint vertex index is outside the positions array")
        fixed = np.zeros(len(positions), dtype=bool) if pinned_mask is None else pinned_mask
        if fixed.shape != (len(positions),) or fixed.dtype != np.dtype(bool):
            raise ValueError("pinned_mask must have shape (n,) and Boolean values")
        if fixed[self.i] and fixed[self.j]:
            return positions
        delta = positions[self.j] - positions[self.i]
        distance = float(np.linalg.norm(delta))
        if distance <= 1e-8:
            return positions
        correction = (distance - self.rest_length) / distance * delta * self.stiffness
        if fixed[self.i]:
            positions[self.j] -= correction
        elif fixed[self.j]:
            positions[self.i] += correction
        else:
            positions[self.i] += correction * 0.5
            positions[self.j] -= correction * 0.5
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
    if not np.all(np.isfinite(vertices)):
        raise ValueError("vertices must contain only finite values")
    if faces.ndim != 2 or faces.shape[1] != 3:
        raise ValueError("faces must have shape (m, 3)")
    if not np.issubdtype(faces.dtype, np.integer):
        raise TypeError("faces must contain integer vertex indices")
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


def solve_constraints(
    positions: np.ndarray,
    constraints: Iterable[Constraint],
    iterations: int = 2,
    pinned_indices: Optional[Iterable[int]] = None,
) -> np.ndarray:
    """Apply all constraints for a fixed number of iterations while preserving fixed vertices."""
    if not isinstance(iterations, int) or isinstance(iterations, bool) or iterations < 0:
        raise ValueError("iterations must be a non-negative integer")
    solved = np.asarray(positions, dtype=np.float32).copy()
    if solved.ndim != 2 or solved.shape[1] != 3:
        raise ValueError("positions must have shape (n, 3)")
    if not np.all(np.isfinite(solved)):
        raise ValueError("positions must contain only finite values")
    fixed = _pinned_mask(pinned_indices, len(solved))
    reusable_constraints = tuple(constraints)
    for _ in range(iterations):
        for constraint in reusable_constraints:
            solved = constraint.solve(solved, fixed)
    return solved

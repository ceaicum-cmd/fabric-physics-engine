"""Mesh visualization helpers."""

from __future__ import annotations

from typing import Any, Dict

import numpy as np


def mesh_bounds(mesh: Dict[str, np.ndarray]) -> Dict[str, Any]:
    """Return simple bounds for a mesh without requiring a rendering backend."""
    vertices = np.asarray(mesh["vertices"], dtype=float)
    if vertices.ndim != 2 or vertices.shape[1] != 3 or len(vertices) == 0:
        raise ValueError("mesh vertices must have shape (n, 3) with at least one vertex")
    if not np.all(np.isfinite(vertices)):
        raise ValueError("mesh vertices must contain only finite values")
    faces = np.asarray(mesh.get("faces", np.empty((0, 3), dtype=int)))
    if faces.ndim != 2 or faces.shape[1] != 3:
        raise ValueError("mesh faces must have shape (m, 3)")
    if not np.issubdtype(faces.dtype, np.integer):
        raise TypeError("mesh faces must contain integer vertex indices")
    if faces.size and (np.any(faces < 0) or np.any(faces >= len(vertices))):
        raise IndexError("face vertex index is outside the mesh")
    return {
        "min": vertices.min(axis=0).tolist(),
        "max": vertices.max(axis=0).tolist(),
        "center": vertices.mean(axis=0).tolist(),
        "vertex_count": int(vertices.shape[0]),
        "face_count": int(faces.shape[0]),
    }

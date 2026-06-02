"""Mesh visualization helpers."""

from __future__ import annotations

from typing import Any, Dict

import numpy as np


def mesh_bounds(mesh: Dict[str, np.ndarray]) -> Dict[str, Any]:
    """Return simple bounds for a mesh without requiring a rendering backend."""
    vertices = np.asarray(mesh["vertices"], dtype=float)
    return {
        "min": vertices.min(axis=0).tolist(),
        "max": vertices.max(axis=0).tolist(),
        "center": vertices.mean(axis=0).tolist(),
        "vertex_count": int(vertices.shape[0]),
        "face_count": int(np.asarray(mesh.get("faces", [])).shape[0]),
    }

"""Fabric material definitions used by simulations and prompt modules."""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from enum import Enum
from typing import Any, Dict

import numpy as np


class MaterialType(str, Enum):
    """Supported fabric material categories."""

    COTTON = "cotton"
    SILK = "silk"
    DENIM = "denim"
    LEATHER = "leather"
    CHIFFON = "chiffon"
    KNIT = "knit"


@dataclass
class FabricProperties:
    """Physical and visual properties for a fabric."""

    material_type: MaterialType
    density: float
    stretch: float
    stiffness: float
    damping: float
    thickness: float
    friction: float
    wrinkle_tendency: float
    sheen: float = 0.0

    def __post_init__(self) -> None:
        """Reject invalid physical coefficients early."""
        self.material_type = MaterialType(self.material_type)
        positive = ("density", "thickness")
        unit_interval = ("stretch", "stiffness", "damping", "friction", "wrinkle_tendency", "sheen")
        for field_name in positive:
            value = getattr(self, field_name)
            if not np.isfinite(value) or value <= 0:
                raise ValueError(f"{field_name} must be a finite value greater than zero")
        for field_name in unit_interval:
            value = getattr(self, field_name)
            if not np.isfinite(value) or not 0 <= value <= 1:
                raise ValueError(f"{field_name} must be a finite value between 0 and 1")

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["material_type"] = self.material_type.value
        return data


FABRIC_LIBRARY: Dict[str, FabricProperties] = {
    "cotton": FabricProperties(
        MaterialType.COTTON, 0.45, 0.30, 0.55, 0.18, 0.0020, 0.55, 0.60, 0.10
    ),
    "silk": FabricProperties(
        MaterialType.SILK, 0.25, 0.18, 0.20, 0.10, 0.0008, 0.30, 0.45, 0.85
    ),
    "denim": FabricProperties(
        MaterialType.DENIM, 0.75, 0.12, 0.85, 0.28, 0.0030, 0.75, 0.35, 0.05
    ),
    "leather": FabricProperties(
        MaterialType.LEATHER, 0.90, 0.08, 0.92, 0.22, 0.0040, 0.65, 0.20, 0.55
    ),
    "chiffon": FabricProperties(
        MaterialType.CHIFFON, 0.12, 0.22, 0.08, 0.08, 0.0004, 0.22, 0.75, 0.35
    ),
    "knit": FabricProperties(
        MaterialType.KNIT, 0.35, 0.70, 0.25, 0.24, 0.0018, 0.50, 0.40, 0.12
    ),
}


def get_fabric_properties(name: str) -> FabricProperties:
    """Return fabric properties by name."""
    key = name.lower().strip()
    if key not in FABRIC_LIBRARY:
        available = ", ".join(sorted(FABRIC_LIBRARY))
        raise KeyError(f"Unknown fabric '{name}'. Available fabrics: {available}")
    fabric = FABRIC_LIBRARY[key]
    return replace(fabric)

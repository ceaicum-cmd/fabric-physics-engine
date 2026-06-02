"""Fabric material definitions used by simulations and prompt modules."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Dict


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

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["material_type"] = self.material_type.value
        return data


FABRIC_LIBRARY: Dict[str, FabricProperties] = {
    "cotton": FabricProperties(MaterialType.COTTON, density=0.45, stretch=0.30, stiffness=0.55, damping=0.18, thickness=0.0020, friction=0.55, wrinkle_tendency=0.60, sheen=0.10),
    "silk": FabricProperties(MaterialType.SILK, density=0.25, stretch=0.18, stiffness=0.20, damping=0.10, thickness=0.0008, friction=0.30, wrinkle_tendency=0.45, sheen=0.85),
    "denim": FabricProperties(MaterialType.DENIM, density=0.75, stretch=0.12, stiffness=0.85, damping=0.28, thickness=0.0030, friction=0.75, wrinkle_tendency=0.35, sheen=0.05),
    "leather": FabricProperties(MaterialType.LEATHER, density=0.90, stretch=0.08, stiffness=0.92, damping=0.22, thickness=0.0040, friction=0.65, wrinkle_tendency=0.20, sheen=0.55),
    "chiffon": FabricProperties(MaterialType.CHIFFON, density=0.12, stretch=0.22, stiffness=0.08, damping=0.08, thickness=0.0004, friction=0.22, wrinkle_tendency=0.75, sheen=0.35),
    "knit": FabricProperties(MaterialType.KNIT, density=0.35, stretch=0.70, stiffness=0.25, damping=0.24, thickness=0.0018, friction=0.50, wrinkle_tendency=0.40, sheen=0.12),
}


def get_fabric_properties(name: str) -> FabricProperties:
    """Return fabric properties by name."""
    key = name.lower().strip()
    if key not in FABRIC_LIBRARY:
        available = ", ".join(sorted(FABRIC_LIBRARY))
        raise KeyError(f"Unknown fabric '{name}'. Available fabrics: {available}")
    fabric = FABRIC_LIBRARY[key]
    return FabricProperties(**fabric.to_dict())

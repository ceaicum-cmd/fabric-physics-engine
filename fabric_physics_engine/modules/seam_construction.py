"""Seam construction prompt module."""

from dataclasses import asdict, dataclass
from typing import Any, Dict


@dataclass
class SeamConstruction:
    """Seam behavior and garment construction controls."""

    name: str = "Seam Construction"
    description: str = "Seam constraints, stitching logic, edge thickness, and garment construction integrity"
    seam_tension: float = 0.75
    edge_thickness: float = 0.7
    stitch_visibility: float = 0.45
    construction_integrity: float = 0.9

    def generate_prompt(self) -> str:
        return (
            f"Seams: tension {self.seam_tension}, edge thickness {self.edge_thickness}, "
            f"stitch visibility {self.stitch_visibility}, construction integrity {self.construction_integrity}"
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

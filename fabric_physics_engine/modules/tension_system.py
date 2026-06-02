"""Fabric tension prompt module."""

from dataclasses import asdict, dataclass
from typing import Any, Dict


@dataclass
class TensionSystem:
    """Directional tension and stretch-map behavior."""

    name: str = "Tension System"
    description: str = "Directional stretch, seam pull, and tautness gradients"
    tension_strength: float = 0.7
    anisotropic_stretch: bool = True
    anchor_point_awareness: float = 0.85
    stress_line_visibility: float = 0.55

    def generate_prompt(self) -> str:
        mode = "anisotropic" if self.anisotropic_stretch else "uniform"
        return (
            f"Tension: {mode} stretch fields, strength {self.tension_strength}, "
            f"anchor awareness {self.anchor_point_awareness}, visible stress lines {self.stress_line_visibility}"
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

"""Gravity-driven fabric behavior module."""

from dataclasses import asdict, dataclass
from typing import Any, Dict


@dataclass
class GravitySystem:
    """Controls visible gravity effects on cloth."""

    name: str = "Gravity System"
    description: str = "Gravity sag, drape direction, and downward cloth settling"
    gravity_strength: float = 9.81
    vertical_drape_bias: float = 0.8
    hem_weighting: float = 0.6
    sag_preservation: bool = True

    def generate_prompt(self) -> str:
        return (
            f"Gravity: {self.gravity_strength:.2f}m/s² downward drape, "
            f"vertical bias {self.vertical_drape_bias}, hem weighting {self.hem_weighting}, "
            f"natural sag {'preserved' if self.sag_preservation else 'reduced'}"
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

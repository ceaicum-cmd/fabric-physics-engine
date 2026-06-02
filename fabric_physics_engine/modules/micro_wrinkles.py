"""Micro wrinkles module."""

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class MicroWrinkles:
    """Fine detail wrinkle generation."""

    name: str = "Micro Wrinkles"
    description: str = "Fine-scale wrinkle and texture details"

    # Wrinkle parameters
    micro_wrinkle_density: float = 0.7
    wrinkle_scale: float = 0.3
    wrinkle_randomness: float = 0.4
    surface_texture_detail: float = 0.8

    # Wrinkle types
    random_surface_creases: bool = True
    fabric_grain_wrinkles: bool = True
    stress_point_wrinkles: bool = True

    def generate_prompt(self) -> str:
        """Generate prompt text for AI model."""
        effects = []
        if self.random_surface_creases:
            effects.append("surface creases")
        if self.fabric_grain_wrinkles:
            effects.append("grain wrinkles")
        if self.stress_point_wrinkles:
            effects.append("stress wrinkles")

        return (
            f"Micro wrinkles: density {self.micro_wrinkle_density}, "
            f"scale {self.wrinkle_scale}, "
            f"randomness {self.wrinkle_randomness}, "
            f"texture detail {self.surface_texture_detail}, "
            f"types: {', '.join(effects)}"
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "micro_wrinkle_density": self.micro_wrinkle_density,
            "wrinkle_scale": self.wrinkle_scale,
            "wrinkle_randomness": self.wrinkle_randomness,
            "surface_texture_detail": self.surface_texture_detail,
            "random_surface_creases": self.random_surface_creases,
            "fabric_grain_wrinkles": self.fabric_grain_wrinkles,
            "stress_point_wrinkles": self.stress_point_wrinkles,
        }

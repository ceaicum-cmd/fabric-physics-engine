"""Cinematic realism module."""

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class CinematicRealism:
    """Cinematic and photoreal enhancement."""

    name: str = "Cinematic Realism"
    description: str = "Cinematic quality and photoreal rendering enhancement"

    # Cinematic parameters
    lighting_interaction: float = 0.9
    subsurface_scattering: bool = True
    fabric_specularity: float = 0.4
    shadow_detail: float = 0.85
    ambient_occlusion_depth: float = 0.7

    # Realism effects
    shows_fabric_luminosity: bool = True
    creates_realistic_shadows: bool = True
    shows_fabric_translucence: bool = True
    maintains_color_accuracy: bool = True

    def generate_prompt(self) -> str:
        """Generate prompt text for AI model."""
        effects = []
        if self.shows_fabric_luminosity:
            effects.append("accurate luminosity")
        if self.creates_realistic_shadows:
            effects.append("realistic shadows")
        if self.shows_fabric_translucence:
            effects.append("light translucence")
        if self.maintains_color_accuracy:
            effects.append("color accuracy")

        return (
            f"Cinematic realism: lighting interaction {self.lighting_interaction}, "
            f"subsurface scattering {'enabled' if self.subsurface_scattering else 'disabled'}, "
            f"specularity {self.fabric_specularity}, "
            f"shadow detail {self.shadow_detail}, "
            f"AO depth {self.ambient_occlusion_depth}, "
            f"effects: {', '.join(effects)}"
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "lighting_interaction": self.lighting_interaction,
            "subsurface_scattering": self.subsurface_scattering,
            "fabric_specularity": self.fabric_specularity,
            "shadow_detail": self.shadow_detail,
            "ambient_occlusion_depth": self.ambient_occlusion_depth,
            "shows_fabric_luminosity": self.shows_fabric_luminosity,
            "creates_realistic_shadows": self.creates_realistic_shadows,
            "shows_fabric_translucence": self.shows_fabric_translucence,
            "maintains_color_accuracy": self.maintains_color_accuracy,
        }

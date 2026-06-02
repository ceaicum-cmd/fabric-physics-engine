"""Layering interaction prompt module."""

from dataclasses import asdict, dataclass
from typing import Any, Dict


@dataclass
class LayeringInteraction:
    """Multi-layer cloth interaction controls."""

    name: str = "Layering Interaction"
    description: str = "Interaction between overlapping garments and fabric layers"
    layer_separation: float = 0.45
    inter_layer_friction: float = 0.55
    occlusion_shadow_strength: float = 0.7
    outer_layer_dominance: float = 0.65

    def generate_prompt(self) -> str:
        return (
            f"Layering: separation {self.layer_separation}, inter-layer friction {self.inter_layer_friction}, "
            f"occlusion shadows {self.occlusion_shadow_strength}, outer-layer dominance {self.outer_layer_dominance}"
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

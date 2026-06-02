"""Fold hierarchy generation module."""

from dataclasses import asdict, dataclass
from typing import Any, Dict


@dataclass
class FoldGenerationSystem:
    """Hierarchical fold generation for fabric realism."""

    name: str = "Fold Generation"
    description: str = "Primary, secondary, and tertiary fold hierarchy"
    primary_fold_angle: float = 35.0
    secondary_fold_density: float = 0.55
    tertiary_variation: float = 0.25
    fold_direction_consistency: float = 0.8

    def generate_prompt(self) -> str:
        return (
            f"Fold hierarchy: primary folds around {self.primary_fold_angle:.1f} degrees, "
            f"secondary density {self.secondary_fold_density}, fine variation {self.tertiary_variation}, "
            f"directional consistency {self.fold_direction_consistency}"
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

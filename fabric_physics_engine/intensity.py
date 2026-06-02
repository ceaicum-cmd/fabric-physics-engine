"""Intensity presets and configuration for the fabric physics prompt engine."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Dict


class IntensityLevel(str, Enum):
    """Available realism/intensity presets."""

    MINIMAL = "minimal"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CINEMATIC = "cinematic"
    MAXIMUM = "maximum"


@dataclass
class Config:
    """Runtime configuration for prompt-generation modules."""

    intensity: IntensityLevel = IntensityLevel.MEDIUM
    realism_scale: float = 1.0

    enable_gravity: bool = True
    enable_tension: bool = True
    enable_compression: bool = True
    enable_fold_generation: bool = True
    enable_material_control: bool = True
    enable_seam_construction: bool = True
    enable_layering: bool = True
    enable_micro_wrinkles: bool = True
    enable_motion_inertia: bool = True
    enable_anti_artifact: bool = True
    enable_cinematic_realism: bool = True
    enable_body_adaptation: bool = True

    def __post_init__(self) -> None:
        """Normalize and validate configuration values."""
        self.intensity = IntensityLevel(self.intensity)
        if self.realism_scale <= 0:
            raise ValueError("realism_scale must be greater than zero")

    def to_dict(self) -> Dict[str, Any]:
        """Convert the configuration into serializable primitives."""
        data = asdict(self)
        data["intensity"] = self.intensity.value
        return data


_PRESETS: Dict[IntensityLevel, Config] = {
    IntensityLevel.MINIMAL: Config(
        intensity=IntensityLevel.MINIMAL,
        realism_scale=0.45,
        enable_micro_wrinkles=False,
        enable_motion_inertia=False,
        enable_cinematic_realism=False,
    ),
    IntensityLevel.LOW: Config(
        intensity=IntensityLevel.LOW,
        realism_scale=0.70,
        enable_motion_inertia=False,
    ),
    IntensityLevel.MEDIUM: Config(
        intensity=IntensityLevel.MEDIUM,
        realism_scale=1.00,
    ),
    IntensityLevel.HIGH: Config(
        intensity=IntensityLevel.HIGH,
        realism_scale=1.25,
    ),
    IntensityLevel.CINEMATIC: Config(
        intensity=IntensityLevel.CINEMATIC,
        realism_scale=1.50,
    ),
    IntensityLevel.MAXIMUM: Config(
        intensity=IntensityLevel.MAXIMUM,
        realism_scale=1.80,
    ),
}


def get_config_for_intensity(level: IntensityLevel | str) -> Config:
    """Return a copy of the preset configuration for an intensity level."""
    if isinstance(level, str):
        level = IntensityLevel(level.lower().strip())
    preset = _PRESETS[level]
    data = preset.to_dict()
    data["intensity"] = level
    return Config(**data)

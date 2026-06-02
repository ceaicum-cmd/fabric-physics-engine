"""Motion inertia module."""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class MotionInertia:
    """Motion and inertia effects."""
    
    name: str = "Motion Inertia"
    description: str = "Dynamic motion and inertia simulation"
    
    # Motion parameters
    motion_dampening: float = 0.85
    inertia_strength: float = 0.7
    settling_time: float = 2.5
    bounce_reduction: float = 0.8
    
    # Motion effects
    shows_motion_trails: bool = True
    creates_settling_wrinkles: bool = True
    shows_momentum: bool = True
    
    def generate_prompt(self) -> str:
        """Generate prompt text for AI model."""
        effects = []
        if self.shows_motion_trails:
            effects.append("motion trails")
        if self.creates_settling_wrinkles:
            effects.append("settling wrinkles")
        if self.shows_momentum:
            effects.append("momentum")
        
        return (
            f"Motion & inertia: dampening {self.motion_dampening}, "
            f"inertia {self.inertia_strength}, "
            f"settling time {self.settling_time}s, "
            f"bounce reduction {self.bounce_reduction}, "
            f"effects: {', '.join(effects)}"
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "motion_dampening": self.motion_dampening,
            "inertia_strength": self.inertia_strength,
            "settling_time": self.settling_time,
            "bounce_reduction": self.bounce_reduction,
            "shows_motion_trails": self.shows_motion_trails,
            "creates_settling_wrinkles": self.creates_settling_wrinkles,
            "shows_momentum": self.shows_momentum,
        }

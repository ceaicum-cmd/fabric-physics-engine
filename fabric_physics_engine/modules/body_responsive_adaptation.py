"""Body responsive adaptation module."""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class BodyResponsiveAdaptation:
    """Adaptive fabric response to body geometry."""
    
    name: str = "Body Responsive Adaptation"
    description: str = "Fabric adaptation to body shape and movement"
    
    # Adaptation parameters
    body_contact_detection: float = 0.95
    fabric_conformance: float = 0.8
    anatomical_awareness: bool = True
    body_shape_response: float = 0.85
    dynamic_adaptation: bool = True
    
    # Adaptation effects
    hugs_curves: bool = True
    follows_body_movement: bool = True
    creates_anatomical_folds: bool = True
    responds_to_anatomy: bool = True
    
    def generate_prompt(self) -> str:
        """Generate prompt text for AI model."""
        effects = []
        if self.hugs_curves:
            effects.append("curves-fitting")
        if self.follows_body_movement:
            effects.append("body-responsive")
        if self.creates_anatomical_folds:
            effects.append("anatomical folds")
        if self.responds_to_anatomy:
            effects.append("anatomy-aware")
        
        return (
            f"Body adaptation: contact detection {self.body_contact_detection}, "
            f"conformance {self.fabric_conformance}, "
            f"anatomical awareness {'enabled' if self.anatomical_awareness else 'disabled'}, "
            f"body shape response {self.body_shape_response}, "
            f"dynamic adaptation {'enabled' if self.dynamic_adaptation else 'disabled'}, "
            f"effects: {', '.join(effects)}"
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "body_contact_detection": self.body_contact_detection,
            "fabric_conformance": self.fabric_conformance,
            "anatomical_awareness": self.anatomical_awareness,
            "body_shape_response": self.body_shape_response,
            "dynamic_adaptation": self.dynamic_adaptation,
            "hugs_curves": self.hugs_curves,
            "follows_body_movement": self.follows_body_movement,
            "creates_anatomical_folds": self.creates_anatomical_folds,
            "responds_to_anatomy": self.responds_to_anatomy,
        }

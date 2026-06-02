"""Anti-artifact module."""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class AntiArtifact:
    """Artifact prevention and correction."""
    
    name: str = "Anti-Artifact"
    description: str = "Prevention and correction of common AI generation artifacts"
    
    # Artifact prevention
    prevent_painted_on_clothing: bool = True
    prevent_distorted_folds: bool = True
    prevent_impossible_physics: bool = True
    prevent_floating_fabric: bool = True
    prevent_excessive_wrinkles: bool = True
    
    # Parameters
    artifact_detection_threshold: float = 0.7
    correction_strength: float = 0.9
    physics_validation: bool = True
    
    def generate_prompt(self) -> str:
        """Generate prompt text for AI model."""
        preventions = []
        if self.prevent_painted_on_clothing:
            preventions.append("not painted-on")
        if self.prevent_distorted_folds:
            preventions.append("realistic folds only")
        if self.prevent_impossible_physics:
            preventions.append("physically valid")
        if self.prevent_floating_fabric:
            preventions.append("gravity-anchored")
        if self.prevent_excessive_wrinkles:
            preventions.append("no excessive wrinkles")
        
        return (
            f"Anti-artifact protocols: {', '.join(preventions)}, "
            f"detection threshold {self.artifact_detection_threshold}, "
            f"correction strength {self.correction_strength}, "
            f"physics validation {'enabled' if self.physics_validation else 'disabled'}"
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "prevent_painted_on_clothing": self.prevent_painted_on_clothing,
            "prevent_distorted_folds": self.prevent_distorted_folds,
            "prevent_impossible_physics": self.prevent_impossible_physics,
            "prevent_floating_fabric": self.prevent_floating_fabric,
            "prevent_excessive_wrinkles": self.prevent_excessive_wrinkles,
            "artifact_detection_threshold": self.artifact_detection_threshold,
            "correction_strength": self.correction_strength,
            "physics_validation": self.physics_validation,
        }

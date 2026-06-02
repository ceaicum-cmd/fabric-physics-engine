"""Main Fabric Physics Engine orchestrator."""

from __future__ import annotations

from typing import Any, Dict, Optional, Union

from .intensity import Config, IntensityLevel, get_config_for_intensity
from .modules.anti_artifact import AntiArtifact
from .modules.body_responsive_adaptation import BodyResponsiveAdaptation
from .modules.cinematic_realism import CinematicRealism
from .modules.compression_system import CompressionSystem
from .modules.core_fabric_physics import CoreFabricPhysics
from .modules.fold_generation import FoldGenerationSystem
from .modules.gravity_system import GravitySystem
from .modules.layering_interaction import LayeringInteraction
from .modules.material_control import MaterialControl
from .modules.micro_wrinkles import MicroWrinkles
from .modules.motion_inertia import MotionInertia
from .modules.seam_construction import SeamConstruction
from .modules.tension_system import TensionSystem


class FabricPhysicsEngine:
    """Main Fabric Physics Engine for AI image generation."""

    def __init__(self, config: Optional[Config] = None):
        self.config = config or get_config_for_intensity(IntensityLevel.MEDIUM)
        self.core_fabric_physics = CoreFabricPhysics()
        self.gravity_system = GravitySystem()
        self.tension_system = TensionSystem()
        self.compression_system = CompressionSystem()
        self.fold_generation = FoldGenerationSystem()
        self.material_control = MaterialControl()
        self.seam_construction = SeamConstruction()
        self.layering_interaction = LayeringInteraction()
        self.micro_wrinkles = MicroWrinkles()
        self.motion_inertia = MotionInertia()
        self.anti_artifact = AntiArtifact()
        self.cinematic_realism = CinematicRealism()
        self.body_adaptation = BodyResponsiveAdaptation()
        self._apply_intensity_scaling()

    @classmethod
    def from_intensity(cls, intensity: Union[IntensityLevel, str]) -> "FabricPhysicsEngine":
        """Build an engine from a named intensity preset."""
        return cls(get_config_for_intensity(intensity))

    def _apply_intensity_scaling(self) -> None:
        """Apply intensity scaling to selected numeric module parameters."""
        scale = self.config.realism_scale
        self.gravity_system.gravity_strength *= scale
        self.fold_generation.primary_fold_angle *= scale
        self.micro_wrinkles.micro_wrinkle_density *= scale
        self.cinematic_realism.lighting_interaction *= scale

    def generate_prompt(self) -> str:
        """Generate complete prompt text for an AI model."""
        prompts = [self.core_fabric_physics.generate_prompt()]
        if self.config.enable_gravity:
            prompts.append(self.gravity_system.generate_prompt())
        if self.config.enable_tension:
            prompts.append(self.tension_system.generate_prompt())
        if self.config.enable_compression:
            prompts.append(self.compression_system.generate_prompt())
        if self.config.enable_fold_generation:
            prompts.append(self.fold_generation.generate_prompt())
        if self.config.enable_material_control:
            prompts.append(self.material_control.generate_prompt())
        if self.config.enable_seam_construction:
            prompts.append(self.seam_construction.generate_prompt())
        if self.config.enable_layering:
            prompts.append(self.layering_interaction.generate_prompt())
        if self.config.enable_micro_wrinkles:
            prompts.append(self.micro_wrinkles.generate_prompt())
        if self.config.enable_motion_inertia:
            prompts.append(self.motion_inertia.generate_prompt())
        if self.config.enable_anti_artifact:
            prompts.append(self.anti_artifact.generate_prompt())
        if self.config.enable_cinematic_realism:
            prompts.append(self.cinematic_realism.generate_prompt())
        if self.config.enable_body_adaptation:
            prompts.append(self.body_adaptation.generate_prompt())
        return " | ".join(prompts)

    def get_all_modules(self) -> Dict[str, Any]:
        """Get all module configurations."""
        return {
            "core_fabric_physics": self.core_fabric_physics.to_dict(),
            "gravity_system": self.gravity_system.to_dict(),
            "tension_system": self.tension_system.to_dict(),
            "compression_system": self.compression_system.to_dict(),
            "fold_generation": self.fold_generation.to_dict(),
            "material_control": self.material_control.to_dict(),
            "seam_construction": self.seam_construction.to_dict(),
            "layering_interaction": self.layering_interaction.to_dict(),
            "micro_wrinkles": self.micro_wrinkles.to_dict(),
            "motion_inertia": self.motion_inertia.to_dict(),
            "anti_artifact": self.anti_artifact.to_dict(),
            "cinematic_realism": self.cinematic_realism.to_dict(),
            "body_adaptation": self.body_adaptation.to_dict(),
        }

    def export_config(self) -> Dict[str, Any]:
        """Export the complete engine configuration."""
        return {
            "config": self.config.to_dict(),
            "modules": self.get_all_modules(),
            "prompt": self.generate_prompt(),
        }

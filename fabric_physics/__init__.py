"""
Fabric Physics Engine - A modular realism framework for AI image generation
that simulates realistic clothing physics including gravity, tension, 
compression, and folding behavior.
"""

__version__ = "3.0.0"
__author__ = "Fabric Physics Team"

from fabric_physics.engine import FabricPhysicsEngine
from fabric_physics.config import IntensityLevel, Config
from fabric_physics.modules.core import CoreFabricPhysics
from fabric_physics.modules.gravity import GravitySystem
from fabric_physics.modules.tension import TensionSystem
from fabric_physics.modules.compression import CompressionSystem
from fabric_physics.modules.fold_generation import FoldGenerationSystem
from fabric_physics.modules.material_control import MaterialControl
from fabric_physics.modules.seam_construction import SeamConstruction
from fabric_physics.modules.layering import LayeringInteraction
from fabric_physics.modules.micro_wrinkles import MicroWrinkles
from fabric_physics.modules.motion_inertia import MotionInertia
from fabric_physics.modules.anti_artifact import AntiArtifact
from fabric_physics.modules.cinematic_realism import CinematicRealism
from fabric_physics.modules.body_responsive import BodyResponsiveAdaptation

__all__ = [
    "FabricPhysicsEngine",
    "IntensityLevel",
    "Config",
    "CoreFabricPhysics",
    "GravitySystem",
    "TensionSystem",
    "CompressionSystem",
    "FoldGenerationSystem",
    "MaterialControl",
    "SeamConstruction",
    "LayeringInteraction",
    "MicroWrinkles",
    "MotionInertia",
    "AntiArtifact",
    "CinematicRealism",
    "BodyResponsiveAdaptation",
]

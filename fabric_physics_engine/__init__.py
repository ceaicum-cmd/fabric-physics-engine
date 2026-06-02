"""Fabric Physics Engine package."""

from .core import FabricSimulation
from .engine import FabricPhysicsEngine
from .fabrics import FabricProperties, MaterialType, get_fabric_properties
from .intensity import Config, IntensityLevel, get_config_for_intensity
from .physics import ForceField, PhysicsEngine
from .constraints import Constraint, SeamConstraint

__version__ = "0.1.0"

"""Compatibility wrapper for the :mod:`fabric_physics_engine` package."""

from fabric_physics_engine import Config as Config
from fabric_physics_engine import Constraint as Constraint
from fabric_physics_engine import FabricPhysicsEngine as FabricPhysicsEngine
from fabric_physics_engine import FabricProperties as FabricProperties
from fabric_physics_engine import FabricSimulation as FabricSimulation
from fabric_physics_engine import ForceField as ForceField
from fabric_physics_engine import IntensityLevel as IntensityLevel
from fabric_physics_engine import MaterialType as MaterialType
from fabric_physics_engine import PhysicsEngine as PhysicsEngine
from fabric_physics_engine import SeamConstraint as SeamConstraint
from fabric_physics_engine import get_config_for_intensity as get_config_for_intensity
from fabric_physics_engine import get_fabric_properties as get_fabric_properties

__all__ = [
    "Config",
    "Constraint",
    "FabricPhysicsEngine",
    "FabricProperties",
    "FabricSimulation",
    "ForceField",
    "IntensityLevel",
    "MaterialType",
    "PhysicsEngine",
    "SeamConstraint",
    "get_config_for_intensity",
    "get_fabric_properties",
]

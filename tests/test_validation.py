import numpy as np
import pytest

from fabric_physics_engine import FabricSimulation, PhysicsEngine, get_fabric_properties
from fabric_physics_engine.constraints import Constraint, build_edge_constraints
from fabric_physics_engine.intensity import Config, get_config_for_intensity
from fabric_physics_engine.models import ShirtModel
from fabric_physics_engine.rendering import mesh_bounds


def test_fabric_lookup_returns_independent_enum_backed_copy():
    first = get_fabric_properties(" cotton ")
    second = get_fabric_properties("cotton")
    first.density = 99
    assert second.material_type.value == "cotton"
    assert second.density != first.density


def test_config_normalizes_input_and_rejects_invalid_scale():
    assert get_config_for_intensity(" HIGH ").intensity.value == "high"
    with pytest.raises(ValueError, match="realism_scale"):
        Config(realism_scale=0)


def test_physics_rejects_invalid_timestep_and_mass():
    engine = PhysicsEngine()
    positions = np.zeros((1, 3), dtype=np.float32)
    velocities = np.zeros_like(positions)
    with pytest.raises(ValueError, match="dt"):
        engine.integrate(positions, velocities, np.ones(1), 0)
    with pytest.raises(ValueError, match="masses"):
        engine.integrate(positions, velocities, np.zeros(1), 0.1)


def test_pinned_vertices_remain_stationary():
    shirt = ShirtModel(get_fabric_properties("cotton"))
    simulation = FabricSimulation()
    simulation.add_garment(shirt)
    before = simulation.get_mesh()["vertices"]
    simulation.step(dt=0.1)
    after = simulation.get_mesh()["vertices"]
    np.testing.assert_array_equal(after[shirt.get_pinned_vertices()], before[shirt.get_pinned_vertices()])


def test_constraint_and_mesh_validation():
    with pytest.raises(ValueError, match="distinct"):
        Constraint(0, 0, 1)
    with pytest.raises(IndexError, match="outside"):
        build_edge_constraints(np.zeros((2, 3)), np.array([[0, 1, 2]]))
    with pytest.raises(ValueError, match="at least one"):
        mesh_bounds({"vertices": np.empty((0, 3))})

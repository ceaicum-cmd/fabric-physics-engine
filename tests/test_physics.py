from fabric_physics_engine import FabricPhysicsEngine, FabricSimulation, IntensityLevel, get_fabric_properties
from fabric_physics_engine.models import ShirtModel


def test_prompt_engine_generates_prompt():
    engine = FabricPhysicsEngine.from_intensity(IntensityLevel.MEDIUM)
    prompt = engine.generate_prompt()
    assert "Gravity" in prompt
    assert "Tension" in prompt
    assert "Anti-artifact" in prompt


def test_simulation_steps_shirt():
    shirt = ShirtModel(get_fabric_properties("cotton"))
    simulation = FabricSimulation()
    simulation.add_garment(shirt)
    simulation.step()
    mesh = simulation.get_mesh()
    assert mesh["vertices"].shape[1] == 3
    assert mesh["faces"].shape[1] == 3

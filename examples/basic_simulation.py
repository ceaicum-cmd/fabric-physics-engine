"""Basic fabric simulation example."""

from fabric_physics_engine import FabricSimulation, get_fabric_properties
from fabric_physics_engine.models import ShirtModel


def main() -> None:
    cotton = get_fabric_properties("cotton")
    shirt = ShirtModel(cotton)
    simulation = FabricSimulation()
    simulation.add_garment(shirt)

    for _ in range(60):
        simulation.step(dt=1 / 60)

    mesh = simulation.get_mesh()
    print(f"vertices={mesh['vertices'].shape[0]} faces={mesh['faces'].shape[0]}")


if __name__ == "__main__":
    main()

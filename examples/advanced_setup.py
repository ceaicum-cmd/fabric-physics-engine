"""Advanced prompt-engine setup example."""

from fabric_physics_engine import FabricPhysicsEngine, IntensityLevel


def main() -> None:
    engine = FabricPhysicsEngine.from_intensity(IntensityLevel.CINEMATIC)
    print(engine.generate_prompt())
    print(engine.export_config()["config"])


if __name__ == "__main__":
    main()

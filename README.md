# Fabric Physics Engine

[![CI](https://github.com/fabric-physics-engine/fabric-physics-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/fabric-physics-engine/fabric-physics-engine/actions/workflows/ci.yml)

Fabric Physics Engine is a lightweight Python toolkit for two related workflows:

1. **Prompt realism orchestration** — compose modular fabric-behavior instructions for AI image generation and editing.
2. **Deterministic cloth simulation** — run a small particle-and-constraint simulation for garment prototyping, examples, and pipeline smoke tests.

The package deliberately keeps the runtime small: NumPy is its only required dependency. It is suitable as a reusable library, a command-line tool, and a documented reference implementation.

## Features

- Six built-in material presets: cotton, silk, denim, leather, chiffon, and knit.
- Six prompt intensity levels, from `minimal` to `maximum`.
- Thirteen prompt modules covering gravity, tension, compression, folds, materials, seams, layering, wrinkles, inertia, artifact resistance, cinematic realism, and body adaptation.
- Shirt and dress meshes with pinned vertices and edge-distance constraints.
- Validated semi-implicit Euler integration with drag and velocity limiting.
- JSON-friendly exports, mesh-bound summaries, CLI commands, automated tests, linting, package builds, and CI.

## Installation

```bash
python -m pip install -e .
```

For development tools:

```bash
python -m pip install -e '.[dev]'
```

## CLI quick start

Generate a prompt:

```bash
fabric-physics prompt --intensity cinematic
```

Export the complete prompt-engine configuration:

```bash
fabric-physics prompt --intensity high --json
```

Run a local simulation smoke test:

```bash
fabric-physics simulate --garment dress --fabric silk --steps 120
```

The same CLI is available without installing its console script:

```bash
python -m fabric_physics_engine simulate --garment shirt --fabric cotton
```

## Python API

### Build an AI-image realism prompt

```python
from fabric_physics_engine import FabricPhysicsEngine, IntensityLevel

engine = FabricPhysicsEngine.from_intensity(IntensityLevel.CINEMATIC)
print(engine.generate_prompt())
config = engine.export_config()
```

### Simulate a garment

```python
from fabric_physics_engine import FabricSimulation, get_fabric_properties
from fabric_physics_engine.models import ShirtModel
from fabric_physics_engine.rendering import mesh_bounds

shirt = ShirtModel(get_fabric_properties("cotton"))
simulation = FabricSimulation()
simulation.add_garment(shirt)

for _ in range(60):
    simulation.step(dt=1 / 60)

print(mesh_bounds(simulation.get_mesh()))
```

## Development

Run the production checks locally:

```bash
ruff check .
pytest
python -m build
```

The GitHub Actions workflow runs those checks on Python 3.9 and Python 3.12 for pull requests and pushes to `main`.

## Documentation map

- Full specification: [`docs/spec/fabric-physics-engine-v3.md`](docs/spec/fabric-physics-engine-v3.md)
- Physics model: [`docs/physics_model.md`](docs/physics_model.md)
- Prompt module library: [`docs/modules/`](docs/modules/)
- Prompt templates: [`docs/templates/`](docs/templates/)
- Prompt-builder workflow: [`docs/workflows/prompt-builder-mvp.md`](docs/workflows/prompt-builder-mvp.md)
- Evaluation scorecard: [`docs/evaluation/scorecard.md`](docs/evaluation/scorecard.md)
- Benchmark runbook: [`docs/benchmarks/runbook.md`](docs/benchmarks/runbook.md)

## License

Released under the [MIT License](LICENSE).

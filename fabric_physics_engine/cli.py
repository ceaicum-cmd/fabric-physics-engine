"""Command-line interface for prompt generation and simulation smoke tests."""

from __future__ import annotations

import argparse
import json
from typing import Sequence

from .core import FabricSimulation
from .engine import FabricPhysicsEngine
from .fabrics import FABRIC_LIBRARY, get_fabric_properties
from .intensity import IntensityLevel
from .models import DressModel, ShirtModel
from .rendering import mesh_bounds


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="fabric-physics", description="Fabric physics prompt and simulation toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    prompt = subparsers.add_parser("prompt", help="generate a realism prompt")
    prompt.add_argument("--intensity", choices=[level.value for level in IntensityLevel], default="medium")
    prompt.add_argument("--json", action="store_true", help="emit the complete engine configuration as JSON")

    simulate = subparsers.add_parser("simulate", help="run a lightweight garment simulation")
    simulate.add_argument("--garment", choices=("shirt", "dress"), default="shirt")
    simulate.add_argument("--fabric", choices=sorted(FABRIC_LIBRARY), default="cotton")
    simulate.add_argument("--steps", type=int, default=60)
    simulate.add_argument("--dt", type=float, default=1 / 60)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Execute the command-line interface."""
    args = _build_parser().parse_args(argv)
    if args.command == "prompt":
        engine = FabricPhysicsEngine.from_intensity(args.intensity)
        print(json.dumps(engine.export_config(), indent=2) if args.json else engine.generate_prompt())
        return 0

    if args.steps < 0:
        raise SystemExit("--steps must be greater than or equal to zero")
    fabric = get_fabric_properties(args.fabric)
    model = ShirtModel(fabric) if args.garment == "shirt" else DressModel(fabric)
    simulation = FabricSimulation()
    simulation.add_garment(model)
    for _ in range(args.steps):
        simulation.step(dt=args.dt)
    print(json.dumps(mesh_bounds(simulation.get_mesh()), indent=2))
    return 0

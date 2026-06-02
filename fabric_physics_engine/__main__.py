"""Allow ``python -m fabric_physics_engine`` to invoke the CLI."""

from .cli import main

raise SystemExit(main())

import argparse
from pathlib import Path

from .scaffold import create_project


def cmd_init(args: argparse.Namespace) -> int:
    """Initialize a new project."""

    project_dir = Path(args.name)

    create_project(
        project_name=args.name,
        project_dir=project_dir,
    )

    print(f"Created project: {project_dir}")

    return 0

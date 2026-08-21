import argparse

from .scaffold import create_project


def cmd_init(args: argparse.Namespace) -> int:
    """Initialize a new project."""

    project_dir = create_project(args.name)

    print(f"Created project: {project_dir}")

    return 0

import argparse


def cmd_init(args: argparse.Namespace) -> int:
    """Initialize a new project."""
    print(f"Creating project: {args.name}")
    return 0

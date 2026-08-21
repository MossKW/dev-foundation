import argparse

from .doctor import doctor_report
from .init import cmd_init
from .version import __version__


def cmd_version(_: argparse.Namespace) -> int:
    """Print package version."""
    print(f"dev-foundation {__version__}")
    return 0


def cmd_doctor(_: argparse.Namespace) -> int:
    """Show environment information."""
    print(doctor_report())
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dev-foundation",
        description="Development foundation toolkit.",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        metavar="COMMAND",
    )

    version_parser = subparsers.add_parser(
        "version",
        help="Show package version.",
    )
    version_parser.set_defaults(func=cmd_version)

    doctor_parser = subparsers.add_parser(
        "doctor",
        help="Show environment information.",
    )
    doctor_parser.set_defaults(func=cmd_doctor)

    init_parser = subparsers.add_parser(
        "init",
        help="Initialize a new project.",
    )
    init_parser.add_argument(
        "name",
        help="Project name.",
    )
    init_parser.set_defaults(func=cmd_init)

    return parser

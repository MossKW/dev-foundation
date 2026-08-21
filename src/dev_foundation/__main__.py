import argparse

from . import __version__
from .doctor import doctor_report


def cmd_version(_: argparse.Namespace) -> int:
    """Print package version."""
    print(f"dev-foundation {__version__}")
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
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if hasattr(args, "func"):
        return args.func(args)

    parser.print_help()
    return 0


def cmd_doctor(_: argparse.Namespace) -> int:
    """Show environment information."""
    print(doctor_report())
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

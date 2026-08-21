import argparse

from .commands.doctor import DoctorCommand
from .commands.init import InitCommand
from .commands.version import VersionCommand


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dev-foundation",
        description="Development foundation toolkit.",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        metavar="COMMAND",
    )

    # Built-in commands
    VersionCommand().register(subparsers)
    DoctorCommand().register(subparsers)
    InitCommand().register(subparsers)

    return parser

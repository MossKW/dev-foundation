import argparse

from .command_registry import commands


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dev-foundation",
        description="Development foundation toolkit.",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        metavar="COMMAND",
    )

    for command in commands():
        command.register(subparsers)

    return parser

"""Application entry point."""

from __future__ import annotations

import argparse

from .command_registry import commands
from .runtime import Runtime


class Application:
    """Top-level application."""

    def __init__(self) -> None:
        self.runtime = Runtime()

    def build_parser(self) -> argparse.ArgumentParser:
        """Build the platform CLI parser."""
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

    def run(self) -> None:
        """Run the application."""
        self.runtime.run()

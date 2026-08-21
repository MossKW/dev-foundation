"""Version command."""

from __future__ import annotations

import argparse

from dev_foundation.commands.base import Command
from dev_foundation.version import __version__


class VersionCommand(Command):
    """Register the version command."""

    def register(self, subparsers: argparse._SubParsersAction) -> None:
        """Register the version command."""
        parser = subparsers.add_parser(
            "version",
            help="Show package version.",
        )
        parser.set_defaults(func=self.run)

    @staticmethod
    def run(_: argparse.Namespace) -> int:
        """Execute the version command."""
        print(f"dev-foundation {__version__}")
        return 0

"""Plugins command."""

from __future__ import annotations

import argparse

from dev_foundation.commands.base import Command


class PluginsCommand(Command):
    """Register the plugins command."""

    def register(self, subparsers: argparse._SubParsersAction) -> None:
        """Register the plugins command."""
        parser = subparsers.add_parser(
            "plugins",
            help="List installed plugins.",
        )
        parser.set_defaults(func=self.run)

    @staticmethod
    def run(_: argparse.Namespace) -> int:
        """Execute the plugins command."""
        print("Installed plugins")
        print("  (none)")
        return 0

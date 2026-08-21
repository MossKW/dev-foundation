"""Init command."""

from __future__ import annotations

import argparse

from dev_foundation.commands.base import Command
from dev_foundation.init import cmd_init


class InitCommand(Command):
    """Initialize a new project."""

    name = "init"
    help = "Initialize a new project."

    def register(self, subparsers: argparse._SubParsersAction) -> None:
        parser = subparsers.add_parser(
            self.name,
            help=self.help,
        )

        parser.add_argument(
            "name",
            help="Project name.",
        )

        parser.set_defaults(func=self.run)

    def run(self, args: argparse.Namespace) -> int:
        return cmd_init(args)

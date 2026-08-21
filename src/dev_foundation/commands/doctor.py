"""Doctor command."""

from __future__ import annotations

import argparse

from dev_foundation.commands.base import Command
from dev_foundation.doctor import doctor_report


class DoctorCommand(Command):
    """Register the doctor command."""

    def register(self, subparsers: argparse._SubParsersAction) -> None:
        """Register the doctor subcommand."""
        parser = subparsers.add_parser(
            "doctor",
            help="Show environment information.",
        )
        parser.set_defaults(func=self.run)

    @staticmethod
    def run(_: argparse.Namespace) -> int:
        """Execute the doctor command."""
        print(doctor_report())
        return 0

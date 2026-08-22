"""Registry of built-in CLI commands."""

from __future__ import annotations

from dev_foundation.commands.base import Command
from dev_foundation.commands.doctor import DoctorCommand
from dev_foundation.commands.init import InitCommand
from dev_foundation.commands.version import VersionCommand

_COMMANDS: list[type[Command]] = [
    VersionCommand,
    DoctorCommand,
    InitCommand,
]


def commands() -> list[Command]:
    """Return instantiated commands."""
    return [command() for command in _COMMANDS]

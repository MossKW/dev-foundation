"""Registry of built-in CLI commands."""

from __future__ import annotations

from importlib.metadata import entry_points

from dev_foundation.commands.base import Command
from dev_foundation.commands.doctor import DoctorCommand
from dev_foundation.commands.init import InitCommand
from dev_foundation.commands.version import VersionCommand

_COMMANDS: list[type[Command]] = [
    VersionCommand,
    DoctorCommand,
    InitCommand,
]


def _plugin_commands() -> list[type[Command]]:
    """Load command plugins from entry points."""

    discovered: list[type[Command]] = []

    for ep in entry_points(group="dev_foundation.commands"):
        discovered.append(ep.load())

    return discovered


def commands() -> list[Command]:
    """Return instantiated commands."""

    command_types = [
        *_COMMANDS,
        *_plugin_commands(),
    ]

    return [command() for command in command_types]

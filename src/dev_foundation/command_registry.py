"""Registry of built-in CLI commands."""

from __future__ import annotations

from dev_foundation.commands.base import Command
from dev_foundation.commands.doctor import DoctorCommand
from dev_foundation.commands.init import InitCommand
from dev_foundation.commands.plugins import PluginsCommand
from dev_foundation.commands.version import VersionCommand
from dev_foundation.plugins.loader import PluginLoader

_COMMANDS: list[type[Command]] = [
    VersionCommand,
    DoctorCommand,
    InitCommand,
]

_COMMANDS = [
    VersionCommand,
    DoctorCommand,
    InitCommand,
    PluginsCommand,
]


def _plugin_commands() -> list[type[Command]]:
    """Load command plugins from entry points."""

    discovered: list[type[Command]] = []

    loader = PluginLoader()

    for ep in loader.discover():
        discovered.append(ep.load())

    return discovered


def commands() -> list[Command]:
    """Return instantiated commands."""

    command_types = [
        *_COMMANDS,
        *_plugin_commands(),
    ]

    return [command() for command in command_types]

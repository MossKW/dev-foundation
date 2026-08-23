"""Registry of built-in CLI commands."""

from __future__ import annotations

from dev_foundation.commands.base import Command
from dev_foundation.commands.doctor import DoctorCommand
from dev_foundation.commands.init import InitCommand
from dev_foundation.commands.plugins import PluginsCommand
from dev_foundation.commands.version import VersionCommand
from dev_foundation.plugin_registry import PluginRegistry


class CommandRegistry:
    """Registry of available CLI commands."""

    _BUILTIN_COMMANDS: tuple[type[Command], ...] = (
        VersionCommand,
        DoctorCommand,
        InitCommand,
        PluginsCommand,
    )

    def __init__(self) -> None:
        self.registry = PluginRegistry()

    def plugin_commands(self) -> list[type[Command]]:
        """Load command plugins."""

        commands: list[type[Command]] = []

        for plugin in self.registry.plugin_types():
            if issubclass(plugin, Command):
                commands.append(plugin)

        return commands

    def command_types(self) -> list[type[Command]]:
        """Return all available command types."""

        return [
            *self._BUILTIN_COMMANDS,
            *self.plugin_commands(),
        ]

    def commands(self) -> list[Command]:
        """Return instantiated commands."""

        return [command() for command in self.command_types()]


def commands() -> list[Command]:
    """Compatibility wrapper."""

    return CommandRegistry().commands()

from unittest.mock import Mock

from dev_foundation.command_registry import CommandRegistry
from dev_foundation.commands.version import VersionCommand


def test_plugin_commands() -> None:
    registry = CommandRegistry()

    registry.registry.plugin_types = Mock(return_value=[VersionCommand])

    commands = registry.plugin_commands()

    assert commands == [VersionCommand]


def test_plugin_commands_ignore_non_command() -> None:
    registry = CommandRegistry()

    registry.registry.plugin_types = Mock(return_value=[object])

    assert registry.plugin_commands() == []

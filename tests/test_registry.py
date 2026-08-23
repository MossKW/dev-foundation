from unittest.mock import Mock, patch

from dev_foundation.blueprint import PythonBlueprint
from dev_foundation.blueprint_registry import blueprints
from dev_foundation.command_registry import commands
from dev_foundation.commands.doctor import DoctorCommand
from dev_foundation.commands.init import InitCommand
from dev_foundation.commands.plugins import PluginsCommand
from dev_foundation.commands.version import VersionCommand
from dev_foundation.plugin_registry import PluginRegistry
from dev_foundation.registry import BlueprintRegistry


def test_registry_default_blueprint() -> None:
    registry = BlueprintRegistry()

    blueprint = registry.get("python")

    assert isinstance(blueprint, PythonBlueprint)


def test_registry_names() -> None:
    registry = BlueprintRegistry()

    assert registry.names() == ["python"]


def test_command_registry() -> None:
    registered = commands()

    assert len(registered) == 4

    assert isinstance(registered[0], VersionCommand)
    assert isinstance(registered[1], DoctorCommand)
    assert isinstance(registered[2], InitCommand)
    assert isinstance(registered[3], PluginsCommand)


@patch.object(PluginRegistry, "plugin_types")
def test_command_registry_plugins(mock_plugin_types) -> None:
    mock_plugin_types.return_value = [VersionCommand]

    registered = commands()

    assert len(registered) == 5

    assert isinstance(registered[0], VersionCommand)
    assert isinstance(registered[1], DoctorCommand)
    assert isinstance(registered[2], InitCommand)
    assert isinstance(registered[3], PluginsCommand)
    assert isinstance(registered[4], VersionCommand)

    mock_plugin_types.assert_called_once()


def test_blueprint_registry() -> None:
    registered = blueprints()

    assert len(registered) == 1
    assert isinstance(registered[0], PythonBlueprint)


@patch("dev_foundation.blueprints.loader.entry_points")
def test_blueprint_registry_plugins(mock_entry_points) -> None:
    plugin = Mock()
    plugin.load.return_value = PythonBlueprint

    mock_entry_points.return_value = [plugin]

    registered = blueprints()

    assert len(registered) == 2
    assert isinstance(registered[-1], PythonBlueprint)

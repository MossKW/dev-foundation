from dev_foundation.blueprint import PythonBlueprint
from dev_foundation.command_registry import commands
from dev_foundation.commands.doctor import DoctorCommand
from dev_foundation.commands.init import InitCommand
from dev_foundation.commands.version import VersionCommand
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

    assert len(registered) == 3
    assert isinstance(registered[0], VersionCommand)
    assert isinstance(registered[1], DoctorCommand)
    assert isinstance(registered[2], InitCommand)

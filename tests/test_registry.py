from dev_foundation.blueprint import PythonBlueprint
from dev_foundation.registry import BlueprintRegistry


def test_registry_default_blueprint() -> None:
    registry = BlueprintRegistry()

    blueprint = registry.get("python")

    assert isinstance(blueprint, PythonBlueprint)


def test_registry_names() -> None:
    registry = BlueprintRegistry()

    assert registry.names() == ["python"]

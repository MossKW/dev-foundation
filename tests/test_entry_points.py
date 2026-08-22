from importlib.metadata import entry_points


def test_command_entry_points_declared() -> None:
    eps = entry_points(group="dev_foundation.commands")

    assert eps is not None


def test_blueprint_entry_points_declared() -> None:
    eps = entry_points(group="dev_foundation.blueprints")

    assert eps is not None

from dev_foundation.blueprint import PythonBlueprint


def test_python_blueprint_name() -> None:
    blueprint = PythonBlueprint()

    assert blueprint.name == "python"

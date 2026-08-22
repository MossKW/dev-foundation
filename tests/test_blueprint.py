from pathlib import Path

from dev_foundation.blueprint import PythonBlueprint


def test_python_blueprint(tmp_path: Path) -> None:
    blueprint = PythonBlueprint()

    blueprint.render("demo-project", tmp_path)

    assert (tmp_path / "README.md").exists()
    assert (tmp_path / "pyproject.toml").exists()
    assert (tmp_path / ".gitignore").exists()

    package_dir = tmp_path / "src" / "demo_project"

    assert (package_dir / "__init__.py").exists()
    assert (package_dir / "__main__.py").exists()

    assert (tmp_path / "tests" / "__init__.py").exists()

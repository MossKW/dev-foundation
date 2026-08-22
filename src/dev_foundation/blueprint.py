"""Built-in Python project blueprint."""

from __future__ import annotations

from pathlib import Path

from .blueprints.base import Blueprint
from .generated_file import GeneratedFile
from .generator import ProjectGenerator
from .template_loader import render_template


class PythonBlueprint(Blueprint):
    """Default Python project blueprint."""

    name = "python"

    def render(self, project_name: str, project_dir: Path) -> None:
        """Generate a Python project."""

        package_name = project_name.replace("-", "_")

        context = {
            "project_name": project_name,
            "package_name": package_name,
        }

        src_dir = project_dir / "src" / package_name
        tests_dir = project_dir / "tests"

        src_dir.mkdir(parents=True, exist_ok=True)
        tests_dir.mkdir(parents=True, exist_ok=True)

        files = [
            GeneratedFile(
                path=project_dir / "README.md",
                content=render_template("README.md", context),
            ),
            GeneratedFile(
                path=project_dir / "pyproject.toml",
                content=render_template("pyproject.toml.tmpl", context),
            ),
            GeneratedFile(
                path=project_dir / ".gitignore",
                content=render_template("gitignore.txt", context),
            ),
            GeneratedFile(
                path=src_dir / "__init__.py",
                content=render_template("package_init.py.tmpl", context),
            ),
            GeneratedFile(
                path=src_dir / "__main__.py",
                content=render_template("package_main.py.tmpl", context),
            ),
            GeneratedFile(
                path=tests_dir / "__init__.py",
                content="",
            ),
        ]

        ProjectGenerator().generate(files)

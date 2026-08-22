"""Built-in Python project blueprint."""

from __future__ import annotations

from pathlib import Path

from .blueprints.base import Blueprint
from .template_loader import render_template
from .writer import ProjectWriter


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

        writer = ProjectWriter()

        src_dir = project_dir / "src" / package_name
        tests_dir = project_dir / "tests"

        src_dir.mkdir(parents=True, exist_ok=True)
        tests_dir.mkdir(parents=True, exist_ok=True)

        writer.write(
            project_dir / "README.md",
            render_template("README.md", context),
        )

        writer.write(
            project_dir / "pyproject.toml",
            render_template("pyproject.toml.tmpl", context),
        )

        writer.write(
            project_dir / ".gitignore",
            render_template("gitignore.txt", context),
        )

        writer.write(
            src_dir / "__init__.py",
            render_template("package_init.py.tmpl", context),
        )

        writer.write(
            src_dir / "__main__.py",
            render_template("package_main.py.tmpl", context),
        )

        writer.write(
            tests_dir / "__init__.py",
            "",
        )

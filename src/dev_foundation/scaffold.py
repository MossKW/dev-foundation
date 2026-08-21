from pathlib import Path

from .template_loader import render_template


def create_project(project_name: str, project_dir: Path) -> None:
    """Create a Python project scaffold."""

    package_name = project_name.replace("-", "_")

    context = {
        "project_name": project_name,
        "package_name": package_name,
    }

    src_dir = project_dir / "src" / package_name
    tests_dir = project_dir / "tests"

    src_dir.mkdir(parents=True, exist_ok=True)
    tests_dir.mkdir(parents=True, exist_ok=True)

    (project_dir / "README.md").write_text(
        render_template("README.md", context),
        encoding="utf-8",
    )

    (project_dir / "pyproject.toml").write_text(
        render_template("pyproject.toml.tmpl", context),
        encoding="utf-8",
    )

    (project_dir / ".gitignore").write_text(
        render_template("gitignore.txt", context),
        encoding="utf-8",
    )

    (src_dir / "__init__.py").write_text(
        render_template("package_init.py.tmpl", context),
        encoding="utf-8",
    )

    (src_dir / "__main__.py").write_text(
        render_template("package_main.py.tmpl", context),
        encoding="utf-8",
    )

    (tests_dir / "__init__.py").write_text(
        "",
        encoding="utf-8",
    )

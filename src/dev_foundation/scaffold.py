from pathlib import Path


def create_project(project_name: str) -> Path:
    """Create a new project."""

    project_dir = Path(project_name)

    project_dir.mkdir(parents=True, exist_ok=False)

    create_layout(project_dir)
    create_files(project_dir)
    create_package(project_dir)

    return project_dir


def create_layout(project_dir: Path) -> None:
    """Create the initial directory layout."""

    (project_dir / "src").mkdir()
    (project_dir / "tests").mkdir()


def create_files(project_dir: Path) -> None:
    """Create the initial project files."""

    create_readme(project_dir)
    create_gitignore(project_dir)
    create_pyproject(project_dir)


def create_package(project_dir: Path) -> None:
    """Create the Python package."""

    package_name = project_dir.name.replace("-", "_")

    package_dir = project_dir / "src" / package_name

    package_dir.mkdir()

    (package_dir / "__init__.py").write_text(
        '__version__ = "0.1.0"\n',
        encoding="utf-8",
    )

    (package_dir / "__main__.py").write_text(
        """def main() -> None:
    print("Hello from package!")


if __name__ == "__main__":
    main()
""",
        encoding="utf-8",
    )

    (project_dir / "tests" / "__init__.py").write_text(
        "",
        encoding="utf-8",
    )


def create_readme(project_dir: Path) -> None:
    """Create README.md."""

    (project_dir / "README.md").write_text(
        f"# {project_dir.name}\n",
        encoding="utf-8",
    )


def create_gitignore(project_dir: Path) -> None:
    """Create .gitignore."""

    (project_dir / ".gitignore").write_text(
        "__pycache__/\n*.py[cod]\n.pytest_cache/\n.coverage\n.venv/\n",
        encoding="utf-8",
    )


def create_pyproject(project_dir: Path) -> None:
    """Create pyproject.toml."""

    content = f"""[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_dir.name}"
version = "0.1.0"
description = ""
readme = "README.md"
requires-python = ">=3.11"
license = "MIT"

[tool.setuptools]
package-dir = {{"" = "src"}}

[tool.setuptools.packages.find]
where = ["src"]
"""

    (project_dir / "pyproject.toml").write_text(
        content,
        encoding="utf-8",
    )

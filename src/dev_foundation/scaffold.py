from pathlib import Path


def create_project(project_name: str) -> Path:
    """Create a new project layout."""

    project_dir = Path(project_name)

    project_dir.mkdir(parents=True, exist_ok=False)

    create_layout(project_dir)

    return project_dir


def create_layout(project_dir: Path) -> None:
    """Create the initial project directory layout."""

    (project_dir / "src").mkdir()

    (project_dir / "tests").mkdir()

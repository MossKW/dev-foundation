from pathlib import Path


def create_project(project_name: str) -> Path:
    """Create a new project directory.

    Currently only creates the project root directory.
    """

    project_dir = Path(project_name)

    project_dir.mkdir(parents=True, exist_ok=False)

    return project_dir

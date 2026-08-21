from pathlib import Path

from .registry import BlueprintRegistry


def create_project(project_name: str, project_dir: Path) -> None:
    """Create a project using the default blueprint."""

    registry = BlueprintRegistry()

    blueprint = registry.get("python")

    blueprint.render(
        project_name=project_name,
        project_dir=project_dir,
    )

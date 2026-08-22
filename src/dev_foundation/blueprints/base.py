"""Base class for project blueprints."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class Blueprint(ABC):
    """Base class for project blueprints."""

    name: str

    @abstractmethod
    def render(
        self,
        project_name: str,
        project_dir: Path,
    ) -> None:
        """Generate the project."""

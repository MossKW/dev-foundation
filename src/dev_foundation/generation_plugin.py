"""Generation plugin API."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from .generator import ProjectGenerator


class GenerationPlugin(ABC):
    """Base class for generation plugins."""

    name: str

    @abstractmethod
    def generate(
        self,
        project_name: str,
        project_dir: Path,
        generator: ProjectGenerator,
    ) -> None:
        """Generate project content."""

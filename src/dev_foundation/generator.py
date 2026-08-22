"""Project generator."""

from __future__ import annotations

from collections.abc import Iterable

from .generated_file import GeneratedFile
from .writer import ProjectWriter


class ProjectGenerator:
    """Generate project files."""

    def __init__(self, writer: ProjectWriter | None = None) -> None:
        self._writer = writer or ProjectWriter()

    def generate(self, files: Iterable[GeneratedFile]) -> None:
        """Generate all project files."""

        for file in files:
            self._writer.write_file(file)

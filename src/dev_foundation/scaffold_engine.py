"""Scaffold engine."""

from __future__ import annotations

from dev_foundation.generated_file import GeneratedFile
from dev_foundation.writer import ProjectWriter


class ScaffoldEngine:
    """Write generated files to disk."""

    def __init__(self) -> None:
        self.writer = ProjectWriter()

    def write(
        self,
        files: list[GeneratedFile],
    ) -> None:
        """Write generated files."""

        for file in files:
            self.writer.write_file(file)

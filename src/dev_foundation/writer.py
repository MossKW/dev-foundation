"""Project file writer."""

from __future__ import annotations

from pathlib import Path

from .generated_file import GeneratedFile


class ProjectWriter:
    """Write generated project files."""

    def write(self, path: Path, content: str) -> None:
        """Write UTF-8 text to a file."""

        path.write_text(content, encoding="utf-8")

    def write_file(self, file: GeneratedFile) -> None:
        """Write a generated file."""

        self.write(file.path, file.content)

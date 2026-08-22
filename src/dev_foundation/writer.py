"""Project file writer."""

from __future__ import annotations

from pathlib import Path


class ProjectWriter:
    """Write project files."""

    def write(self, path: Path, content: str) -> None:
        """Write UTF-8 text to a file."""

        path.write_text(content, encoding="utf-8")

"""Generated project file model."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class GeneratedFile:
    """Represents a generated project file."""

    path: Path
    content: str

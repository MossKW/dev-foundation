"""Rendering context."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RenderContext:
    """Context passed to template rendering."""

    project_name: str
    package_name: str

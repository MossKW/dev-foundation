"""Metadata helpers."""

from __future__ import annotations

from dataclasses import dataclass
from importlib.metadata import entry_points as _entry_points


@dataclass(slots=True)
class PluginMetadata:
    """Metadata describing a plugin."""

    name: str
    version: str
    description: str = ""
    author: str = ""


def entry_points():
    """Return installed entry points."""
    return _entry_points()

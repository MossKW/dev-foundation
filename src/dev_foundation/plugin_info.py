"""Plugin metadata."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class PluginInfo:
    """Metadata describing a plugin."""

    name: str
    version: str
    description: str
    author: str

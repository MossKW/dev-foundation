"""Blueprint plugin loader."""

from __future__ import annotations

from importlib.metadata import entry_points

from .base import Blueprint


class BlueprintLoader:
    """Load blueprint plugins."""

    def load(self) -> list[type[Blueprint]]:
        discovered: list[type[Blueprint]] = []

        for ep in entry_points(group="dev_foundation.blueprints"):
            discovered.append(ep.load())

        return discovered

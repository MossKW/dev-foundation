"""Blueprint registry."""

from __future__ import annotations

from dev_foundation.blueprint_registry import blueprints


class BlueprintRegistry:
    """Registry for project blueprints."""

    def __init__(self) -> None:
        self._blueprints = {blueprint.name: blueprint for blueprint in blueprints()}

    def get(self, name: str):
        """Return a blueprint by name."""
        return self._blueprints[name]

    def names(self) -> list[str]:
        """Return registered blueprint names."""
        return sorted(self._blueprints)

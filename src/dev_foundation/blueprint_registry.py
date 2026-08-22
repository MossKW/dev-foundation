"""Registry of project blueprints."""

from __future__ import annotations

from dev_foundation.blueprint import PythonBlueprint
from dev_foundation.blueprints.base import Blueprint
from dev_foundation.blueprints.loader import BlueprintLoader


class BlueprintRegistry:
    """Registry of available project blueprints."""

    _BUILTIN_BLUEPRINTS: tuple[type[Blueprint], ...] = (PythonBlueprint,)

    def blueprint_types(self) -> list[type[Blueprint]]:
        """Return all available blueprint types."""

        return [
            *self._BUILTIN_BLUEPRINTS,
            *BlueprintLoader().load(),
        ]

    def blueprints(self) -> list[Blueprint]:
        """Return instantiated blueprints."""

        return [blueprint() for blueprint in self.blueprint_types()]


def blueprints() -> list[Blueprint]:
    """Compatibility wrapper."""

    return BlueprintRegistry().blueprints()

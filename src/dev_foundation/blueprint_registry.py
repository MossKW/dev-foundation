"""Registry of project blueprints."""

from __future__ import annotations

from dev_foundation.blueprint import PythonBlueprint
from dev_foundation.blueprints.base import Blueprint
from dev_foundation.blueprints.loader import BlueprintLoader

_BLUEPRINTS: list[type[Blueprint]] = [
    PythonBlueprint,
]


def blueprints() -> list[Blueprint]:
    """Return instantiated blueprints."""

    blueprint_types = [
        *_BLUEPRINTS,
        *BlueprintLoader().load(),
    ]

    return [blueprint() for blueprint in blueprint_types]

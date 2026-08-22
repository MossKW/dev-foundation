"""Registry of built-in project blueprints."""

from __future__ import annotations

from dev_foundation.blueprint import PythonBlueprint
from dev_foundation.blueprints.base import Blueprint

_BLUEPRINTS: list[type[Blueprint]] = [
    PythonBlueprint,
]


def blueprints() -> list[Blueprint]:
    """Return instantiated blueprints."""

    return [blueprint() for blueprint in _BLUEPRINTS]

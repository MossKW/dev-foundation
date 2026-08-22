"""Blueprint plugin API."""

from __future__ import annotations

from typing import Protocol

from .blueprints.base import Blueprint


class BlueprintPlugin(Protocol):
    """Protocol for blueprint plugins."""

    def load(self) -> Blueprint:
        """Return a blueprint instance."""

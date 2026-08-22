"""Plugin API."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from .commands.base import Command


@runtime_checkable
class CommandPlugin(Protocol):
    """Protocol for command plugins."""

    def load(self) -> Command:
        """Return a command instance."""

"""Plugin API."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from .commands.base import Command
from .metadata import PluginMetadata


@runtime_checkable
class CommandPlugin(Protocol):
    """Protocol for command plugins."""

    metadata: PluginMetadata

    def load(self) -> Command:
        """Return a command instance."""

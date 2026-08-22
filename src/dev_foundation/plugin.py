"""Plugin base protocols."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from .generation_plugin import GenerationPlugin
from .metadata import PluginMetadata


@runtime_checkable
class CommandPlugin(Protocol):
    """Protocol for command plugins."""

    metadata: PluginMetadata

    def load(self) -> None:
        """Load plugin."""


class Plugin(GenerationPlugin):
    """Base class for generation plugins."""

    metadata: PluginMetadata

    def load(self) -> None:
        """Load plugin."""

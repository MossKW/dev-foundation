"""Plugin manager."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .plugin_registry import PluginRegistry
from .plugins.base import BasePlugin

if TYPE_CHECKING:
    from .runtime_context import RuntimeContext


class PluginManager:
    """Manage plugin discovery and registration."""

    def __init__(self) -> None:
        self.registry = PluginRegistry()

    def discover(self) -> list[type[BasePlugin]]:
        """Discover available plugins."""
        return self.registry.plugin_types()

    def load(self) -> list[BasePlugin]:
        """Load discovered plugins."""
        return self.registry.plugins()

    def register(
        self,
        context: RuntimeContext,
    ) -> None:
        """Register all loaded plugins."""
        for plugin in self.load():
            plugin.register(context)

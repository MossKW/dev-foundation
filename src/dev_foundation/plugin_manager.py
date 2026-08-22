"""Plugin manager."""

from __future__ import annotations

from importlib.metadata import EntryPoint
from typing import TYPE_CHECKING

from .plugins.base import BasePlugin
from .plugins.loader import PluginLoader

if TYPE_CHECKING:
    from .runtime_context import RuntimeContext


class PluginManager:
    """Manage plugin discovery and registration."""

    def __init__(self) -> None:
        self.loader = PluginLoader()
        self.entry_points: list[EntryPoint] = []

    def discover(self) -> list[EntryPoint]:
        """Discover available plugins."""
        self.entry_points = self.loader.discover()
        return self.entry_points

    def load(self) -> list[BasePlugin]:
        """Load discovered plugins."""
        plugins: list[BasePlugin] = []

        for entry_point in self.discover():
            plugin = entry_point.load()()
            plugins.append(plugin)

        return plugins

    def register(
        self,
        context: RuntimeContext,
    ) -> None:
        """Register all loaded plugins."""
        for plugin in self.load():
            plugin.register(context)

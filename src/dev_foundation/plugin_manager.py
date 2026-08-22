"""Plugin manager."""

from __future__ import annotations

from importlib.metadata import EntryPoint

from .plugins.loader import PluginLoader


class PluginManager:
    """Manage plugin discovery."""

    def __init__(self) -> None:
        self.loader = PluginLoader()
        self._entry_points: list[EntryPoint] = []
        self._plugins: list[type] = []

    def discover(self) -> list[EntryPoint]:
        """Discover available plugins."""
        self._entry_points = self.loader.discover()
        return list(self._entry_points)

    def load(self) -> list[type]:
        """Load discovered plugins."""
        self._plugins = [entry_point.load() for entry_point in self._entry_points]
        return list(self._plugins)

    def plugins(self) -> list[type]:
        """Return loaded plugins."""
        return list(self._plugins)

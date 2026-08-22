"""Plugin manager."""

from __future__ import annotations

from importlib.metadata import EntryPoint

from .plugins.loader import PluginLoader


class PluginManager:
    """Manage plugin discovery."""

    def __init__(self) -> None:
        self.loader = PluginLoader()
        self._plugins: list[EntryPoint] = []

    def discover(self) -> list[EntryPoint]:
        """Discover available plugins."""
        self._plugins = self.loader.discover()
        return self._plugins

    def plugins(self) -> list[EntryPoint]:
        """Return discovered plugins."""
        return list(self._plugins)

"""Plugin manager."""

from __future__ import annotations

from importlib.metadata import EntryPoint

from .plugins.loader import PluginLoader


class PluginManager:
    """Manage plugin discovery."""

    def __init__(self) -> None:
        self.loader = PluginLoader()

    def discover(self) -> list[EntryPoint]:
        """Discover available plugins."""
        return self.loader.discover()

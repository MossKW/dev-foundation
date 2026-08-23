"""Framework discovery services."""

from __future__ import annotations

from importlib.metadata import EntryPoint

from dev_foundation.blueprints.loader import BlueprintLoader
from dev_foundation.plugins.loader import PluginLoader


class Discovery:
    """Central discovery service for framework entry points."""

    def __init__(self) -> None:
        self._plugin_loader = PluginLoader()
        self._blueprint_loader = BlueprintLoader()

    def discover_plugins(self) -> list[EntryPoint]:
        """Return discovered plugin entry points."""
        return self._plugin_loader.discover()

    def discover_blueprints(self) -> list[type]:
        """Return discovered blueprint types."""
        return self._blueprint_loader.load()

"""Plugin registry."""

from __future__ import annotations

from dev_foundation.plugins.base import BasePlugin
from dev_foundation.plugins.loader import PluginLoader


class PluginRegistry:
    """Registry of discovered plugins."""

    def __init__(self) -> None:
        self.loader = PluginLoader()
        self._plugins: list[type[BasePlugin]] | None = None

    def plugin_types(self) -> list[type[BasePlugin]]:
        """Return discovered plugin types."""

        if self._plugins is None:
            self._plugins = [
                entry_point.load() for entry_point in self.loader.discover()
            ]

        return self._plugins

    def plugins(self) -> list[BasePlugin]:
        """Return instantiated plugins."""

        return [plugin() for plugin in self.plugin_types()]

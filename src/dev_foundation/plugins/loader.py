"""Plugin loader."""

from __future__ import annotations

from importlib.metadata import EntryPoint, entry_points


class PluginLoader:
    """Load plugins from entry points."""

    GROUP = "dev_foundation.commands"

    def discover(self) -> list[EntryPoint]:
        """Return discovered command entry points."""
        return list(
            entry_points(
                group=self.GROUP,
            )
        )

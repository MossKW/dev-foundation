"""Runtime context."""

from __future__ import annotations

from .plugin_manager import PluginManager


class RuntimeContext:
    """Shared runtime state.

    The RuntimeContext owns long-lived services that are shared across
    the runtime lifecycle.
    """

    def __init__(self) -> None:
        self.plugin_manager = PluginManager()

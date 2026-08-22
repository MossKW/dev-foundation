"""Runtime context."""

from __future__ import annotations

from .blueprint_registry import BlueprintRegistry
from .command_registry import CommandRegistry
from .plugin_manager import PluginManager


class RuntimeContext:
    """Shared runtime state.

    RuntimeContext owns the long-lived services used during a runtime
    session. It stores shared state but does not coordinate execution.
    """

    def __init__(self) -> None:
        self.plugin_manager = PluginManager()
        self.command_registry = CommandRegistry()
        self.blueprint_registry = BlueprintRegistry()

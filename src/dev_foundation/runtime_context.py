"""Runtime context."""

from __future__ import annotations

from .blueprint_registry import BlueprintRegistry
from .command_registry import CommandRegistry
from .lifecycle import Lifecycle
from .plugin_manager import PluginManager


class RuntimeContext:
    """Shared runtime services."""

    def __init__(self) -> None:
        self.command_registry = CommandRegistry()
        self.blueprint_registry = BlueprintRegistry()
        self.plugin_manager = PluginManager()
        self.lifecycle = Lifecycle()

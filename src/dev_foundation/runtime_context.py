"""Runtime context."""

from __future__ import annotations

from .blueprint_registry import BlueprintRegistry
from .command_registry import CommandRegistry
from .container import Container
from .lifecycle import Lifecycle
from .plugin_manager import PluginManager


class RuntimeContext:
    """Shared runtime services."""

    def __init__(self) -> None:
        self.container = Container()

        self.container.register(CommandRegistry())
        self.container.register(BlueprintRegistry())
        self.container.register(PluginManager())
        self.container.register(Lifecycle())

    @property
    def command_registry(self) -> CommandRegistry:
        """Return the command registry."""
        return self.container.resolve(CommandRegistry)

    @property
    def blueprint_registry(self) -> BlueprintRegistry:
        """Return the blueprint registry."""
        return self.container.resolve(BlueprintRegistry)

    @property
    def plugin_manager(self) -> PluginManager:
        """Return the plugin manager."""
        return self.container.resolve(PluginManager)

    @property
    def lifecycle(self) -> Lifecycle:
        """Return the lifecycle manager."""
        return self.container.resolve(Lifecycle)

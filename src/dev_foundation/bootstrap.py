"""Application bootstrap."""

from __future__ import annotations

from .blueprint_registry import BlueprintRegistry
from .command_registry import CommandRegistry
from .container import Container
from .lifecycle import Lifecycle
from .plugin_manager import PluginManager


def bootstrap(container: Container) -> None:
    """Register core framework services."""

    container.register(CommandRegistry())
    container.register(BlueprintRegistry())
    container.register(PluginManager())
    container.register(Lifecycle())

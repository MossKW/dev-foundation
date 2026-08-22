"""Runtime."""

from __future__ import annotations

from .lifecycle import Lifecycle
from .plugin_manager import PluginManager
from .runtime_context import RuntimeContext


class Runtime:
    """Application runtime."""

    def __init__(self) -> None:
        self.context = RuntimeContext()

    def startup(self) -> None:
        """Initialize the runtime."""
        self.context.container.resolve(
            Lifecycle,
        ).startup()

    def register_plugins(self) -> None:
        """Register all plugins."""
        self.context.container.resolve(
            PluginManager,
        ).register(self.context)

    def register_capabilities(self) -> None:
        """Register plugin capabilities."""

    def run(self) -> None:
        """Run the application."""
        self.startup()
        self.register_plugins()
        self.register_capabilities()
        self.shutdown()

    def shutdown(self) -> None:
        """Shut down the runtime."""
        self.context.container.resolve(
            Lifecycle,
        ).shutdown()

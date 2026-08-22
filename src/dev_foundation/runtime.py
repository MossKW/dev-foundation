"""Platform runtime."""

from __future__ import annotations

from .lifecycle import Lifecycle
from .plugin_manager import PluginManager
from .runtime_context import RuntimeContext


class Runtime:
    """Coordinates platform execution."""

    def __init__(self) -> None:
        self.context = RuntimeContext()

    def run(self) -> None:
        """Execute the runtime lifecycle."""
        self.startup()
        self.discover_plugins()
        self.register_capabilities()
        self.validate()
        self.dispatch()
        self.shutdown()

    def startup(self) -> None:
        """Initialize the runtime."""
        self.context.container.resolve(
            Lifecycle,
        ).startup()

    def discover_plugins(self) -> None:
        """Discover available plugins."""
        self.context.container.resolve(
            PluginManager,
        ).discover()

    def register_capabilities(self) -> None:
        """Register plugin capabilities."""
        pass

    def validate(self) -> None:
        """Validate runtime state."""
        pass

    def dispatch(self) -> None:
        """Dispatch the requested command."""
        pass

    def shutdown(self) -> None:
        """Shut down the runtime."""
        self.context.container.resolve(
            Lifecycle,
        ).shutdown()

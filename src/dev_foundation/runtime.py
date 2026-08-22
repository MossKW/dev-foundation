"""Platform runtime."""

from __future__ import annotations

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
        # Force registry initialization early so the runtime owns them.
        self.context.command_registry.commands()
        self.context.blueprint_registry.blueprints()

    def discover_plugins(self) -> None:
        """Discover available plugins."""
        self.context.plugin_manager.discover()

    def register_capabilities(self) -> None:
        """Register plugin capabilities."""
        # Placeholder for future plugin registration.
        pass

    def validate(self) -> None:
        """Validate runtime state."""
        pass

    def dispatch(self) -> None:
        """Dispatch the requested command."""
        pass

    def shutdown(self) -> None:
        """Shut down the runtime."""
        pass

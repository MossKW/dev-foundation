"""Runtime context."""

from __future__ import annotations

from .blueprint_registry import BlueprintRegistry
from .bootstrap import bootstrap
from .command_registry import CommandRegistry
from .container import Container
from .lifecycle import Lifecycle


class RuntimeContext:
    """Shared runtime services."""

    def __init__(self) -> None:
        self.container = Container()
        bootstrap(self.container)

    @property
    def command_registry(self) -> CommandRegistry:
        """Return the command registry."""
        return self.container.resolve(CommandRegistry)

    @property
    def blueprint_registry(self) -> BlueprintRegistry:
        """Return the blueprint registry."""
        return self.container.resolve(BlueprintRegistry)

    @property
    def lifecycle(self) -> Lifecycle:
        """Return the lifecycle manager."""
        return self.container.resolve(Lifecycle)

"""Base plugin interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from dev_foundation.runtime_context import RuntimeContext


class BasePlugin(ABC):
    """Base class for all plugins."""

    name: ClassVar[str] = "plugin"
    version: ClassVar[str] = "0.1.0"
    description: ClassVar[str] = ""
    author: ClassVar[str] = ""

    @abstractmethod
    def register(
        self,
        context: RuntimeContext,
    ) -> None:
        """Register plugin services."""

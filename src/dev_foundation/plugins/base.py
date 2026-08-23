"""Base plugin interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, ClassVar

from dev_foundation.plugin_info import PluginInfo

if TYPE_CHECKING:
    from dev_foundation.runtime_context import RuntimeContext


class BasePlugin(ABC):
    """Base class for all plugins."""

    name: ClassVar[str] = ""
    version: ClassVar[str] = "0.1.0"
    description: ClassVar[str] = ""
    author: ClassVar[str] = ""

    @classmethod
    def info(cls) -> PluginInfo:
        """Return plugin metadata."""
        return PluginInfo(
            name=cls.name,
            version=cls.version,
            description=cls.description,
            author=cls.author,
        )

    @abstractmethod
    def register(
        self,
        context: RuntimeContext,
    ) -> None:
        """Register plugin capabilities."""

"""Base plugin interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BasePlugin(ABC):
    """Abstract base class for framework plugins."""

    @abstractmethod
    def register(
        self,
        context: Any,
    ) -> None:
        """Register the plugin with the runtime context."""

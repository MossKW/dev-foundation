"""Service container."""

from __future__ import annotations

from typing import Any


class Container:
    """Store runtime services."""

    def __init__(self) -> None:
        self._services: dict[type[Any], Any] = {}

    def register(self, service: Any) -> None:
        """Register a service instance."""
        self._services[type(service)] = service

    def resolve(self, service_type: type[Any]) -> Any:
        """Resolve a registered service."""
        return self._services[service_type]

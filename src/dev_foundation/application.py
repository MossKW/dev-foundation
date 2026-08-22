"""Application entry point."""

from __future__ import annotations

from .runtime import Runtime


class Application:
    """Top-level application."""

    def __init__(self) -> None:
        self.runtime = Runtime()

    def run(self) -> None:
        """Run the application."""
        self.runtime.run()

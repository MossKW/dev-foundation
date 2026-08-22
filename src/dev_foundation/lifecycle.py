"""Runtime lifecycle management."""

from __future__ import annotations


class Lifecycle:
    """Manage runtime lifecycle."""

    def startup(self) -> None:
        """Start the runtime."""
        pass

    def shutdown(self) -> None:
        """Stop the runtime."""
        pass

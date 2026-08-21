"""Base classes for CLI commands."""

from __future__ import annotations

import argparse
from abc import ABC, abstractmethod


class Command(ABC):
    """Base class for all CLI commands."""

    @abstractmethod
    def register(self, subparsers: argparse._SubParsersAction) -> None:
        """Register the command."""

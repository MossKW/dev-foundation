"""Command-line interface."""

from __future__ import annotations

import argparse

from .application import Application


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    return Application().build_parser()

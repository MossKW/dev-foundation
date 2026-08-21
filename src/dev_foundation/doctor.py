"""Environment diagnostics for dev-foundation."""

from __future__ import annotations

import platform
import sys

from .version import __version__


def doctor_report() -> str:
    """Return a human-readable environment report."""
    lines = [
        "Development Foundation Doctor",
        "",
        f"Package    : dev-foundation {__version__}",
        f"Python     : {platform.python_version()}",
        f"Executable : {sys.executable}",
        f"Platform   : {platform.platform()}",
    ]

    return "\n".join(lines)

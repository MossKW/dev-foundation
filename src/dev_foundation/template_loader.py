"""Template loading helpers."""

from __future__ import annotations

from importlib.resources import files

from .template_engine import TemplateEngine

_TEMPLATE_DIR = files("dev_foundation.templates")

_ENGINE = TemplateEngine()


def load_template(name: str) -> str:
    """Load a bundled template."""

    return _TEMPLATE_DIR.joinpath(name).read_text(
        encoding="utf-8",
    )


def render_template(
    name: str,
    context: dict[str, str],
) -> str:
    """Render a bundled template."""

    return _ENGINE.render(
        load_template(name),
        context,
    )

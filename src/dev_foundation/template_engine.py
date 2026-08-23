"""Template rendering engine."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from dev_foundation.render_context import RenderContext


class TemplateEngine:
    """Simple template rendering engine."""

    def render(
        self,
        template: str,
        context: dict[str, str],
    ) -> str:
        """Render a template."""

        rendered = template

        for key, value in context.items():
            rendered = rendered.replace(
                f"{{{{ {key} }}}}",
                value,
            )

        return rendered

    def render_context(
        self,
        template: str,
        context: RenderContext,
    ) -> str:
        """Render a template from a RenderContext."""

        data: dict[str, Any] = asdict(context)

        return self.render(
            template,
            {key: str(value) for key, value in data.items()},
        )

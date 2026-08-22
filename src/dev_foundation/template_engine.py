"""Template rendering engine."""

from __future__ import annotations


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

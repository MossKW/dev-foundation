from importlib.resources import files

_TEMPLATE_DIR = files("dev_foundation.templates")


def load_template(name: str) -> str:
    """Load a bundled template."""

    return _TEMPLATE_DIR.joinpath(name).read_text(encoding="utf-8")


def render_template(name: str, context: dict[str, str]) -> str:
    """Render a template using simple placeholder replacement."""

    content = load_template(name)

    for key, value in context.items():
        content = content.replace(f"{{{{ {key} }}}}", value)

    return content

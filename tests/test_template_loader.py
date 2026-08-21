from importlib.resources import files


def render_template(template_name: str, context: dict[str, str]) -> str:
    template = (
        files("dev_foundation.templates")
        .joinpath(template_name)
        .read_text(encoding="utf-8")
    )

    for key, value in context.items():
        template = template.replace(f"{{{{ {key} }}}}", value)

    return template

from dev_foundation.template_loader import (
    load_template,
    render_template,
)


def test_load_template() -> None:
    template = load_template("README.md")

    assert "{{ project_name }}" in template


def test_render_template() -> None:
    rendered = render_template(
        "README.md",
        {
            "project_name": "demo",
            "package_name": "demo",
        },
    )

    assert "demo" in rendered

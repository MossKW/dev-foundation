from dev_foundation.render_context import RenderContext
from dev_foundation.template_engine import TemplateEngine


def test_render() -> None:
    engine = TemplateEngine()

    rendered = engine.render(
        "Hello {{ name }}!",
        {
            "name": "Moss",
        },
    )

    assert rendered == "Hello Moss!"


def test_render_multiple_values() -> None:
    engine = TemplateEngine()

    rendered = engine.render(
        "{{ greeting }} {{ name }}!",
        {
            "greeting": "Hello",
            "name": "Moss",
        },
    )

    assert rendered == "Hello Moss!"


def test_render_context() -> None:
    engine = TemplateEngine()

    rendered = engine.render_context(
        "{{ project_name }}/{{ package_name }}",
        RenderContext(
            project_name="demo",
            package_name="demo_pkg",
        ),
    )

    assert rendered == "demo/demo_pkg"

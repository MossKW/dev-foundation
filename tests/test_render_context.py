from dev_foundation.render_context import RenderContext


def test_render_context() -> None:
    context = RenderContext(
        project_name="demo",
        package_name="demo_pkg",
    )

    assert context.project_name == "demo"
    assert context.package_name == "demo_pkg"


def test_render_context_repr() -> None:
    context = RenderContext(
        project_name="demo",
        package_name="demo_pkg",
    )

    assert "RenderContext" in repr(context)

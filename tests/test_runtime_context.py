from dev_foundation.runtime_context import RuntimeContext


def test_runtime_context_instantiation() -> None:
    context = RuntimeContext()

    assert context is not None


def test_runtime_context_plugin_manager() -> None:
    context = RuntimeContext()

    assert context.plugin_manager is not None

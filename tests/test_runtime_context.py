from dev_foundation.blueprint_registry import BlueprintRegistry
from dev_foundation.command_registry import CommandRegistry
from dev_foundation.plugin_manager import PluginManager
from dev_foundation.runtime_context import RuntimeContext


def test_runtime_context_instantiation() -> None:
    context = RuntimeContext()

    assert context is not None


def test_runtime_context_plugin_manager() -> None:
    context = RuntimeContext()

    assert isinstance(
        context.plugin_manager,
        PluginManager,
    )


def test_runtime_context_command_registry() -> None:
    context = RuntimeContext()

    assert isinstance(
        context.command_registry,
        CommandRegistry,
    )


def test_runtime_context_blueprint_registry() -> None:
    context = RuntimeContext()

    assert isinstance(
        context.blueprint_registry,
        BlueprintRegistry,
    )

from dev_foundation.blueprint_registry import BlueprintRegistry
from dev_foundation.command_registry import CommandRegistry
from dev_foundation.container import Container
from dev_foundation.lifecycle import Lifecycle
from dev_foundation.plugin_manager import PluginManager
from dev_foundation.runtime_context import RuntimeContext


def test_runtime_context_exposes_container():
    context = RuntimeContext()

    assert isinstance(context.container, Container)


def test_runtime_context_contains_command_registry():
    context = RuntimeContext()

    assert isinstance(
        context.command_registry,
        CommandRegistry,
    )


def test_runtime_context_contains_blueprint_registry():
    context = RuntimeContext()

    assert isinstance(
        context.blueprint_registry,
        BlueprintRegistry,
    )


def test_runtime_context_contains_plugin_manager():
    context = RuntimeContext()

    assert isinstance(
        context.plugin_manager,
        PluginManager,
    )


def test_runtime_context_contains_lifecycle():
    context = RuntimeContext()

    assert isinstance(
        context.lifecycle,
        Lifecycle,
    )

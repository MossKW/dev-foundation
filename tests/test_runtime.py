from dev_foundation.lifecycle import Lifecycle
from dev_foundation.plugin_manager import PluginManager
from dev_foundation.runtime import Runtime


def test_runtime_has_context():
    runtime = Runtime()

    assert runtime.context is not None


def test_runtime_uses_container_services(monkeypatch):
    runtime = Runtime()

    plugin_manager = runtime.context.container.resolve(
        PluginManager,
    )
    lifecycle = runtime.context.container.resolve(
        Lifecycle,
    )

    called = []

    monkeypatch.setattr(
        lifecycle,
        "startup",
        lambda: called.append("startup"),
    )

    monkeypatch.setattr(
        plugin_manager,
        "register",
        lambda context: called.append("register"),
    )

    monkeypatch.setattr(
        lifecycle,
        "shutdown",
        lambda: called.append("shutdown"),
    )

    runtime.run()

    assert called == [
        "startup",
        "register",
        "shutdown",
    ]

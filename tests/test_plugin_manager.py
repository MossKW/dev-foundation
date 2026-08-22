from dev_foundation.plugin_manager import PluginManager
from dev_foundation.plugins.base import BasePlugin
from dev_foundation.runtime_context import RuntimeContext


class DemoPlugin(BasePlugin):
    def register(self, context: RuntimeContext) -> None:
        pass


class FakeEntryPoint:
    def load(self):
        return DemoPlugin


def test_discover_returns_entry_points(monkeypatch):
    manager = PluginManager()

    fake = FakeEntryPoint()

    monkeypatch.setattr(
        manager.loader,
        "discover",
        lambda: [fake],
    )

    assert manager.discover() == [fake]


def test_load_returns_loaded_plugins(monkeypatch):
    manager = PluginManager()

    fake = FakeEntryPoint()

    monkeypatch.setattr(
        manager.loader,
        "discover",
        lambda: [fake],
    )

    plugins = manager.load()

    assert len(plugins) == 1
    assert isinstance(
        plugins[0],
        DemoPlugin,
    )

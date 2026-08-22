from importlib.metadata import EntryPoint

from dev_foundation.plugin_manager import PluginManager


class DemoPlugin:
    pass


class FakeEntryPoint:
    def load(self):
        return DemoPlugin


def test_discover_returns_loader_results(monkeypatch):
    manager = PluginManager()

    expected = [
        EntryPoint(
            name="demo",
            value="demo.plugin:Plugin",
            group="dev_foundation.commands",
        )
    ]

    monkeypatch.setattr(
        manager.loader,
        "discover",
        lambda: expected,
    )

    assert manager.discover() == expected


def test_load_returns_loaded_plugins(monkeypatch):
    manager = PluginManager()

    monkeypatch.setattr(
        manager.loader,
        "discover",
        lambda: [FakeEntryPoint()],
    )

    manager.discover()

    assert manager.load() == [DemoPlugin]
    assert manager.plugins() == [DemoPlugin]

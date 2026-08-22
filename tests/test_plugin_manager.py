from importlib.metadata import EntryPoint

from dev_foundation.plugin_manager import PluginManager


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


def test_plugins_returns_discovered_plugins(monkeypatch):
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

    manager.discover()

    assert manager.plugins() == expected

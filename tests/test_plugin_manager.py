from dev_foundation.plugin_manager import PluginManager


class DemoPlugin:
    def register(self, context):
        pass


def test_discover(monkeypatch):
    manager = PluginManager()

    monkeypatch.setattr(
        manager.registry,
        "plugin_types",
        lambda: [DemoPlugin],
    )

    assert manager.discover() == [DemoPlugin]


def test_load(monkeypatch):
    manager = PluginManager()

    monkeypatch.setattr(
        manager.registry,
        "plugins",
        lambda: [DemoPlugin()],
    )

    plugins = manager.load()

    assert len(plugins) == 1
    assert isinstance(
        plugins[0],
        DemoPlugin,
    )

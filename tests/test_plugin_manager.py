from dev_foundation.plugin_manager import PluginManager


def test_plugin_manager_instantiation() -> None:
    manager = PluginManager()

    assert manager is not None


def test_plugin_manager_discover() -> None:
    manager = PluginManager()

    plugins = manager.discover()

    assert isinstance(plugins, list)

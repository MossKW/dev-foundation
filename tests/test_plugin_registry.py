from unittest.mock import Mock, patch

from dev_foundation.plugin_registry import PluginRegistry


class FakePlugin:
    pass


@patch("dev_foundation.plugins.loader.PluginLoader.discover")
def test_plugin_registry(mock_discover) -> None:
    entry_point = Mock()
    entry_point.load.return_value = FakePlugin

    mock_discover.return_value = [entry_point]

    registry = PluginRegistry()

    assert registry.plugin_types() == [FakePlugin]

    mock_discover.assert_called_once()


@patch("dev_foundation.plugins.loader.PluginLoader.discover")
def test_plugin_registry_plugins(mock_discover) -> None:
    entry_point = Mock()
    entry_point.load.return_value = FakePlugin

    mock_discover.return_value = [entry_point]

    registry = PluginRegistry()

    plugins = registry.plugins()

    assert len(plugins) == 1
    assert isinstance(plugins[0], FakePlugin)


@patch("dev_foundation.plugins.loader.PluginLoader.discover")
def test_plugin_registry_cached_plugins(mock_discover) -> None:
    registry = PluginRegistry()

    registry._plugins = []

    assert registry.plugin_types() == []

    mock_discover.assert_not_called()

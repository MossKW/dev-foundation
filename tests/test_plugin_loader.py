from unittest.mock import patch

from dev_foundation.plugins.loader import PluginLoader


@patch("dev_foundation.plugins.loader.entry_points")
def test_loader_calls_entry_points(mock_entry_points):
    mock_entry_points.return_value = []

    loader = PluginLoader()

    assert loader.discover() == []

    mock_entry_points.assert_called_once_with(
        group="dev_foundation.commands",
    )

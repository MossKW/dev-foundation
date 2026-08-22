from unittest.mock import Mock, patch

from dev_foundation.blueprint import PythonBlueprint
from dev_foundation.blueprints.loader import BlueprintLoader


@patch("dev_foundation.blueprints.loader.entry_points")
def test_blueprint_loader(mock_entry_points):
    plugin = Mock()
    plugin.load.return_value = PythonBlueprint

    mock_entry_points.return_value = [plugin]

    loader = BlueprintLoader()

    loaded = loader.load()

    assert loaded == [PythonBlueprint]

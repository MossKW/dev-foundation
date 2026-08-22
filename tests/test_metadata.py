from unittest.mock import patch

from dev_foundation.metadata import PluginMetadata, entry_points


def test_metadata() -> None:
    metadata = PluginMetadata(
        name="docs",
        version="1.0.0",
        description="Documentation tools",
        author="Moss",
    )

    assert metadata.name == "docs"
    assert metadata.version == "1.0.0"
    assert metadata.description == "Documentation tools"
    assert metadata.author == "Moss"


@patch("dev_foundation.metadata._entry_points")
def test_entry_points(mock_entry_points) -> None:
    mock_entry_points.return_value = []

    assert entry_points() == []

    mock_entry_points.assert_called_once_with()

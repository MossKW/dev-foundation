from dev_foundation.metadata import PluginMetadata
from dev_foundation.plugin import CommandPlugin


def test_command_plugin_protocol() -> None:
    class DummyPlugin:
        metadata = PluginMetadata(
            name="dummy",
            version="0.1.0",
        )

        def load(self):
            return None

    plugin = DummyPlugin()

    assert isinstance(plugin, CommandPlugin)

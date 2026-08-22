from dev_foundation.plugin import CommandPlugin


def test_command_plugin_protocol() -> None:
    class DummyPlugin:
        def load(self):
            return None

    plugin = DummyPlugin()

    assert isinstance(plugin, CommandPlugin)

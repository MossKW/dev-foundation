from dev_foundation.plugin_info import PluginInfo
from dev_foundation.plugins.base import BasePlugin


class DemoPlugin(BasePlugin):
    name = "demo"
    version = "1.0.0"
    description = "Demo plugin"
    author = "Unit Test"

    def register(self, context):
        pass


def test_plugin_info():
    info = DemoPlugin.info()

    assert isinstance(info, PluginInfo)
    assert info.name == "demo"
    assert info.version == "1.0.0"
    assert info.description == "Demo plugin"
    assert info.author == "Unit Test"


def test_plugin_instance():
    plugin = DemoPlugin()

    assert isinstance(plugin, BasePlugin)

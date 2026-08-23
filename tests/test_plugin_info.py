from dev_foundation.plugin_info import PluginInfo
from dev_foundation.plugins.base import BasePlugin


class DemoPlugin(BasePlugin):
    name = "template"
    version = "0.1.0"
    description = "Template engine"
    author = "MossKW"

    def register(self, context):
        pass


def test_plugin_info_fields():
    info = PluginInfo(
        name="template",
        version="0.1.0",
        description="Template engine",
        author="MossKW",
    )

    assert info.name == "template"
    assert info.version == "0.1.0"
    assert info.description == "Template engine"
    assert info.author == "MossKW"


def test_plugin_info_from_plugin():
    info = DemoPlugin.info()

    assert info == PluginInfo(
        name="template",
        version="0.1.0",
        description="Template engine",
        author="MossKW",
    )

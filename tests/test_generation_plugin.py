from pathlib import Path

from dev_foundation.generation_plugin import GenerationPlugin
from dev_foundation.generator import ProjectGenerator


class DummyPlugin(GenerationPlugin):
    name = "dummy"

    def generate(
        self,
        project_name: str,
        project_dir: Path,
        generator: ProjectGenerator,
    ) -> None:
        pass


def test_generation_plugin_api(tmp_path: Path) -> None:
    plugin = DummyPlugin()

    plugin.generate(
        "demo",
        tmp_path,
        ProjectGenerator(),
    )

    assert plugin.name == "dummy"

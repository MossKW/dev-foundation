from pathlib import Path

from dev_foundation.generated_file import GeneratedFile
from dev_foundation.generator import ProjectGenerator


def test_project_generator(tmp_path: Path) -> None:
    generator = ProjectGenerator()

    generator.generate(
        [
            GeneratedFile(
                path=tmp_path / "README.md",
                content="# Demo",
            ),
            GeneratedFile(
                path=tmp_path / "pyproject.toml",
                content="[project]",
            ),
        ]
    )

    assert (tmp_path / "README.md").read_text(encoding="utf-8") == "# Demo"
    assert (tmp_path / "pyproject.toml").read_text(encoding="utf-8") == "[project]"

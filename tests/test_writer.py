from pathlib import Path

from dev_foundation.generated_file import GeneratedFile
from dev_foundation.writer import ProjectWriter


def test_project_writer_writes_file(tmp_path: Path) -> None:
    writer = ProjectWriter()

    target = tmp_path / "hello.txt"

    writer.write(target, "Hello World")

    assert target.exists()
    assert target.read_text(encoding="utf-8") == "Hello World"


def test_project_writer_writes_generated_file(tmp_path: Path) -> None:
    writer = ProjectWriter()

    generated = GeneratedFile(
        path=tmp_path / "README.md",
        content="# Demo",
    )

    writer.write_file(generated)

    assert generated.path.exists()
    assert generated.path.read_text(encoding="utf-8") == "# Demo"

from pathlib import Path

from dev_foundation.generated_file import GeneratedFile


def test_generated_file() -> None:
    file = GeneratedFile(
        path=Path("README.md"),
        content="# Hello",
    )

    assert file.path == Path("README.md")
    assert file.content == "# Hello"

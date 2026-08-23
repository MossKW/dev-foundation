from pathlib import Path
from unittest.mock import Mock

from dev_foundation.generated_file import GeneratedFile
from dev_foundation.scaffold_engine import ScaffoldEngine


def test_scaffold_engine_write() -> None:
    engine = ScaffoldEngine()

    engine.writer = Mock()

    files = [
        GeneratedFile(
            path=Path("README.md"),
            content="# Hello",
        ),
        GeneratedFile(
            path=Path("main.py"),
            content="print('hello')",
        ),
    ]

    engine.write(files)

    assert engine.writer.write_file.call_count == 2

    engine.writer.write_file.assert_any_call(files[0])
    engine.writer.write_file.assert_any_call(files[1])

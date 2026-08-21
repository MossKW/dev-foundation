from dev_foundation.__main__ import main


def test_cli_init(tmp_path, monkeypatch, capsys) -> None:
    monkeypatch.chdir(tmp_path)

    exit_code = main(["init", "my-project"])

    captured = capsys.readouterr()

    project = tmp_path / "my-project"

    assert exit_code == 0
    assert "Created project:" in captured.out

    assert (project / "src").is_dir()
    assert (project / "tests").is_dir()

    assert (project / "README.md").is_file()
    assert (project / ".gitignore").is_file()
    assert (project / "pyproject.toml").is_file()

    package = project / "src" / "my_project"

    assert package.is_dir()
    assert (package / "__init__.py").is_file()
    assert (package / "__main__.py").is_file()

    assert (project / "tests" / "__init__.py").is_file()

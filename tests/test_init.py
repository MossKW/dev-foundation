from dev_foundation.__main__ import main


def test_cli_init(tmp_path, monkeypatch, capsys) -> None:
    monkeypatch.chdir(tmp_path)

    exit_code = main(["init", "my-project"])

    captured = capsys.readouterr()

    project = tmp_path / "my-project"

    assert exit_code == 0

    assert "Created project:" in captured.out

    assert project.exists()
    assert project.is_dir()

    assert (project / "src").is_dir()
    assert (project / "tests").is_dir()

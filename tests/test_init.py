from dev_foundation.__main__ import main


def test_cli_init(tmp_path, monkeypatch, capsys) -> None:
    monkeypatch.chdir(tmp_path)

    exit_code = main(["init", "my-project"])

    captured = capsys.readouterr()

    assert exit_code == 0

    assert "Created project:" in captured.out

    assert (tmp_path / "my-project").exists()

    assert (tmp_path / "my-project").is_dir()

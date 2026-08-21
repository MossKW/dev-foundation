from dev_foundation.__main__ import main


def test_cli_version(capsys) -> None:
    exit_code = main(["version"])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.strip() == "dev-foundation 0.1.0"


def test_cli_help(capsys) -> None:
    exit_code = main([])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Development foundation toolkit." in captured.out
    assert "version" in captured.out

from dev_foundation.__main__ import main


def test_cli_init(capsys) -> None:
    exit_code = main(["init", "my-project"])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Creating project: my-project" in captured.out

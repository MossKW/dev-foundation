from dev_foundation.__main__ import main


def test_plugins_command(capsys) -> None:
    exit_code = main(["plugins"])

    out = capsys.readouterr().out

    assert exit_code == 0
    assert "Installed plugins" in out

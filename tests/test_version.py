from dev_foundation import __version__
from dev_foundation.__main__ import main


def test_version():
    assert __version__ == "0.1.0"


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == f"dev-foundation {__version__}"

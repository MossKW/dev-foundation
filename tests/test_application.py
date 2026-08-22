from dev_foundation.application import Application


def test_application_creates_runtime() -> None:
    app = Application()

    assert app.runtime is not None

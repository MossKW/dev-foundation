from dev_foundation.lifecycle import Lifecycle


def test_startup():
    lifecycle = Lifecycle()

    lifecycle.startup()


def test_shutdown():
    lifecycle = Lifecycle()

    lifecycle.shutdown()

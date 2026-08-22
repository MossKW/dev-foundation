from dev_foundation.runtime import Runtime


def test_runtime_instantiation() -> None:
    runtime = Runtime()

    assert runtime is not None

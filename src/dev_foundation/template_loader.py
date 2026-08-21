from importlib.resources import files

_TEMPLATE_DIR = files("dev_foundation.templates")


def load_template(name: str) -> str:
    """Load a bundled template file."""

    return _TEMPLATE_DIR.joinpath(name).read_text(encoding="utf-8")

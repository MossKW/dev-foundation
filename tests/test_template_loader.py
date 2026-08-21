from dev_foundation.template_loader import load_template


def test_load_readme_template() -> None:
    content = load_template("README.md")

    assert "{{ project_name }}" in content


def test_load_package_template() -> None:
    content = load_template("package_main.py.tmpl")

    assert "def main()" in content

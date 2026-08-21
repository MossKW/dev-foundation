# dev-foundation

> A modern Python project template with testing, linting, formatting, coverage, and GitHub Actions.

---

## Features

- Python 3.11+
- Modern `src` layout
- pytest
- Coverage.py
- Ruff
- Black
- pre-commit
- GitHub Actions CI
- MIT License

---

## Project Structure

```text
dev-foundation/
├── .github/
│   └── workflows/
├── docs/
├── src/
│   └── dev_foundation/
├── tests/
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## Requirements

- Python 3.11 or newer
- pip

---

## Installation

```bash
git clone https://github.com/MossKW/dev-foundation.git

cd dev-foundation

python -m venv .venv

source .venv/bin/activate

python -m pip install --upgrade pip

python -m pip install -e ".[dev]"
```

---

## Usage

```bash
python -m dev_foundation
```

Expected output:

```text
dev-foundation 0.1.0
```

---

## Testing

Run all tests:

```bash
python -m pytest
```

Generate a coverage report:

```bash
coverage run -m pytest

coverage report -m
```

---

## Code Quality

Run all quality checks:

```bash
ruff check .

black --check .

pre-commit run --all-files
```

---

## Continuous Integration

GitHub Actions automatically runs the following checks on every push and pull request:

- Ruff
- Black
- pytest
- Coverage.py
- pre-commit

---

## Development

Before committing code, verify that everything passes locally:

```bash
ruff check .

black --check .

python -m pytest

coverage run -m pytest

coverage report -m

pre-commit run --all-files
```

---

## License

This project is licensed under the MIT License.

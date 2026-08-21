# Contributing to dev-foundation

First of all, thank you for your interest in contributing to **dev-foundation**.

This project aims to provide a modern, reusable Python project foundation with clean architecture, automated quality checks, and engineering best practices.

---

## Development Workflow

1. Fork the repository (if applicable).
2. Create a new branch from `main`.
3. Implement your changes.
4. Run all quality checks.
5. Commit using Conventional Commits.
6. Open a Pull Request.

---

## Branch Naming

Use descriptive branch names.

Examples:

```text
feature/add-cli
feature/update-readme
fix/version-import
docs/improve-contributing
ci/update-workflow
test/add-cli-tests
```

---

## Commit Messages

This project follows the Conventional Commits specification.

Examples:

```text
feat: add CLI entry point
fix: correct version import
docs: improve README
test: add version tests
ci: update GitHub Actions workflow
refactor: simplify package structure
chore: update dependencies
```

---

## Code Style

Before committing, ensure your code passes all quality checks.

```bash
ruff check .

black --check .

python -m pytest

coverage run -m pytest

coverage report -m

pre-commit run --all-files
```

All checks should pass successfully before opening a Pull Request.

---

## Python Style Guide

- Follow PEP 8.
- Use type hints where appropriate.
- Keep functions small and focused.
- Prefer descriptive variable names.
- Write readable code over clever code.

---

## Testing

Every new feature should include tests whenever practical.

Run tests with:

```bash
python -m pytest
```

Generate a coverage report:

```bash
coverage run -m pytest

coverage report -m
```

---

## Pull Requests

Before opening a Pull Request, ensure that:

- All tests pass.
- Coverage does not decrease.
- Ruff reports no issues.
- Black reports no formatting issues.
- pre-commit passes successfully.
- Documentation is updated if necessary.

---

## Reporting Issues

When reporting bugs, please include:

- Operating system
- Python version
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages or logs

---

## Questions

If you have questions or suggestions, feel free to open an Issue or Pull Request.

Thank you for contributing!

"""Tests for application."""

from __future__ import annotations

from dev_foundation.application import Application


def test_build_parser():
    app = Application()

    parser = app.build_parser()

    assert parser.prog == "dev-foundation"


def test_run(monkeypatch):
    app = Application()

    called = []

    monkeypatch.setattr(
        app.runtime,
        "run",
        lambda: called.append("run"),
    )

    app.run()

    assert called == ["run"]

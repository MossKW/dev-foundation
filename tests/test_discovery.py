from dev_foundation.discovery import Discovery


class DemoBlueprint:
    pass


class FakeEntryPoint:
    pass


def test_discover_plugins(monkeypatch):
    discovery = Discovery()

    entry_point = FakeEntryPoint()

    monkeypatch.setattr(
        discovery._plugin_loader,
        "discover",
        lambda: [entry_point],
    )

    assert discovery.discover_plugins() == [entry_point]


def test_discover_blueprints(monkeypatch):
    discovery = Discovery()

    monkeypatch.setattr(
        discovery._blueprint_loader,
        "load",
        lambda: [DemoBlueprint],
    )

    assert discovery.discover_blueprints() == [DemoBlueprint]

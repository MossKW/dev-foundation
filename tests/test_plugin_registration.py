from dev_foundation.plugin_manager import PluginManager


class FakePlugin:
    def register(self, context):
        context.called = True


def test_plugin_manager_register(monkeypatch):
    manager = PluginManager()

    monkeypatch.setattr(
        manager,
        "load",
        lambda: [FakePlugin()],
    )

    class Context:
        called = False

    context = Context()

    manager.register(context)

    assert context.called is True

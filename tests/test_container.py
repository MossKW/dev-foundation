from dev_foundation.container import Container


class DemoService:
    pass


def test_register_and_resolve():
    container = Container()
    service = DemoService()

    container.register(service)

    assert container.resolve(DemoService) is service


def test_register_multiple_services():
    class ServiceA:
        pass

    class ServiceB:
        pass

    container = Container()

    service_a = ServiceA()
    service_b = ServiceB()

    container.register(service_a)
    container.register(service_b)

    assert container.resolve(ServiceA) is service_a
    assert container.resolve(ServiceB) is service_b

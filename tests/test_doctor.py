from dev_foundation.doctor import doctor_report


def test_doctor_report() -> None:
    report = doctor_report()

    assert "Development Foundation Doctor" in report
    assert "Package" in report
    assert "Python" in report
    assert "Executable" in report
    assert "Platform" in report

import hello


def test_main_exists():
    assert hasattr(hello, "main")


def test_always_passes():
    assert True

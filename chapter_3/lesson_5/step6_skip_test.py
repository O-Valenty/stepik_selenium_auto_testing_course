import pytest

@pytest.mark.xfail(strict=True)
def test_success():
    assert True

@pytest.mark.xfail
def test_not_succeed():
    assert False

@pytest.mark.skip
def test_skipped():
    assert False

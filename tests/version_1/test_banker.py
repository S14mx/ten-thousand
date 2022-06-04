import pytest
from ten_thousand.banker import Banker

pytestmark = [pytest.mark.version_1]

@pytest.mark.skip("TODO")
def test_new_banker():
    banker = Banker()
    assert banker.balance == 0
    assert banker.shelved == 0

@pytest.mark.skip("TODO")
def test_shelf():
    banker = Banker()
    banker.shelf(100)
    assert banker.shelved == 100
    assert banker.balance == 0

@pytest.mark.skip("TODO")
def test_deposit():
    banker = Banker()
    banker.shelf(100)
    banker.bank()
    assert banker.shelved == 0
    assert banker.balance == 100

@pytest.mark.skip("TODO")
def test_clear_shelf():
    banker = Banker()
    banker.shelf(100)
    banker.bank()
    banker.shelf(50)
    banker.clear_shelf()
    assert banker.balance == 100
    assert banker.shelved == 0
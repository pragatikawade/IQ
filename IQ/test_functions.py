import pytest
import functions as functions
def test_addn():
    res = functions.addn(10,5)
    assert res ==15

def test_subc():
    r = functions.subc(10,5)
    assert r == 5

def test_devide():
    with pytest.raises(ValueError):
        functions.devideero(10,0)

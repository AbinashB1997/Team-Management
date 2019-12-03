import pytest
import app


@pytest.mark.number # MARKERS => this can be directly used when running a command pytest tes_app.py -v -m number
def test_add():
    assert app.add(2.3, 5.6) == 7.8999999999999995
    assert app.add(2, 0) == 2
    assert app.add(2.3, 0) == 2.3
    assert app.add(2, 5) == 7

@pytest.mark.number
def test_mul():
    assert app.mul(2.3, 5.6) == 12.879999999999999
    assert app.mul(2, 0) == 0
    assert app.mul(2.3, 0) == 0
    assert app.mul(2, 5) == 10

@pytest.mark.number
def test_CeilDiv():
    assert app.CeilDiv(2.3, 5.6) == 1.0
    assert app.CeilDiv(2, 0.1) == 20.0
    assert app.CeilDiv(2.3, 2) == 2.0
    assert app.CeilDiv(2, 5) == 1

@pytest.mark.number
def test_isPrime():
    assert app.isPrime(15) == False
    assert app.isPrime(17) == True

@pytest.mark.string
def test_isPalindrome():
    assert app.isPalindrome("abcba") == True
    assert app.isPalindrome("abcbb") == False
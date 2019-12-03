'''
    2nd way to pass test-cases as parametrize form
'''

import app
import pytest

x = app.demo_class()

@pytest.mark.parametrize('arr, n, result',
    [
        ([1, 1, 1, 1, 0, 0, 0], 7, 4),
        ([1, 1, 1, 0, 0, 0, 0], 7, 3),
        ([1, 0, 0, 0], 4, 1)
    ]
)

def test_countOnes(arr, n, result):
    assert x.countOnes(arr, n) == result

@pytest.mark.parametrize('str1, result',
    [
        ("abcba", True),
        ("aba", True),
        ("abcd", False),
        ("a", True),
        ("", True)
    ]
)

def test_isPalindrome(str1, result):
    assert x.isPalindrome(str1) == result

@pytest.mark.parametrize('num, result',
    [
        (17, True),
        (5, True),
        (12, False),
        (2, True),
        (11, True)
    ]
)

def test_isPrime(num, result):
    assert x.isPrime(num) == result

@pytest.mark.parametrize('num1, num2, result',
    [
        (10, 15, 5),
        (35, 10, 5),
        (31, 2, 1),
        (10, 4, 2),
        (5, 5, 5)
    ]
)

def test_GCD(num1, num2, result):
    assert x.GCD(num1, num2) == result

@pytest.mark.parametrize('num, K, result',
    [
        (10, 2, 14),
        (15, 3, 15)
    ]
)

def test_setKthBit(num, K, result):
    assert x.setKthBit(num, K) == result

@pytest.mark.parametrize('num, result',
    [
        (1, 1),
        (2, 2),
        (50, 20365011074),
        (14, 610),
        (77, 8944394323791464),
        (11, 144)
    ]
)

def test_fibonacci(num, result):
    assert x.fibonacci(num) == result

@pytest.mark.parametrize('num, mod, result',
    [
        ("3982378328623737256363272383732653623327637", 10, 7),
        ("1767251462623553343156443113153644118798162145153", 6, 5),
        ("45678865447345787654478654788768", 22, 10)
    ]
)

def test_mod(num, mod, result):
    assert x.mod(num, mod) == result

@pytest.mark.parametrize('num, result',
    [
        (10, "YES"),
        (12, "NO")
    ]
)

def test_isAlternatePattern(num, result):
    assert x.isAlternatePattern(num) == result

@pytest.mark.parametrize('l, N, result',
    [
        ([3, 5, 2, 4, 6], 5, 7),
        ([1, 2, 3], 3, 2),
        ([1, 2, 3, 4], 4, 0),
        ([251, 16, 1, 33, 13, 4], 6, 0)
    ]
)

def test_XorSubarray(l, N, result):
    assert x.XorSubarray(l, N) == result

@pytest.mark.parametrize('N, result',
    [
        (23, 43),
        (2, 1),
        (84, 168)
    ]
)

def test_swapOddEvenBits(N, result):
    assert x.swapOddEvenBits(N) == result
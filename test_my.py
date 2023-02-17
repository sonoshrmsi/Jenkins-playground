import pytest
from main import *


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3), (5, 4, 9), (6, 7, 13)
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, -1), (5, 4, 1), (6, 7, -1)
])
def test_substract(a, b, expected):
    assert substract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2), (5, 4, 20), (6, 7, 42)
])
def test_multi(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 0.5), (5, 4, 5/4), (6, 7, 6/7)
])
def test_divide(a, b, expected):
    assert divde(a, b) == expected

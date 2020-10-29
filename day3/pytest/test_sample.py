import pytest

# content of test_sample.py
def inc(x):
    return x + 1

@pytest.mark.parametrize("number,expected", [(-5, -4), (3, 4), (0, 1), (5, 7)])
def test_inc(number, expected, someoher):
    assert inc(number) == expected

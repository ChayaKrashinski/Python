import pytest
import main

@pytest.mark.parametrize(("end, res"), [(1, 2), (2, 3), (3, {0, 1})])
def test_find(end, res):
    assert main.find_primes(end) == res

@pytest.mark.spacific
def test_find():
    assert main.find_primes(20) == {0, 1, 3, 7, 9, 11, 13, 15, 17, 19}

def test_sort():
    assert main.sort_list([9, 8, 7]) == {7, 8, 9}


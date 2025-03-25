import pytest

from  Algorithms.CompareTheTriplets import compareTriplets

def test_case_1():
    """Test case 1: a > b in all elements"""
    assert compareTriplets([5, 6, 7], [3, 2, 1]) == [3, 0]

def test_case_2():
    """Test case 2: a < b in all elements"""
    assert compareTriplets([1, 2, 3], [5, 6, 7]) == [0, 3]

def test_case_3():
    """Test case 3: a and b have equal scores in all elements"""
    assert compareTriplets([3, 3, 3], [3, 3, 3]) == [0, 0]

def test_case_4():
    """Test case 4: mixed comparisons"""
    assert compareTriplets([5, 6, 7], [3, 6, 10]) == [1, 1]

def test_case_5():
    """Test case 5: another mixed comparison"""
    assert compareTriplets([17, 28, 30], [99, 16, 8]) == [2, 1]


def test_large_values():
    """Test with large values"""
    assert compareTriplets([100, 100, 100], [1, 1, 1]) == [3, 0]
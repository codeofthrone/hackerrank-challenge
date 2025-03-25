import pytest
from preparation_kit_python.FindTheMedian import findMedian

def test_findMedian_odd_length():
    arr = [5, 3, 1, 2, 4]
    assert findMedian(arr) == 3

def test_findMedian_even_length():
    arr = [1, 2, 3, 4]
    assert findMedian(arr) == 2.5

def test_findMedian_already_sorted():
    arr = [1, 2, 3, 4, 5]
    assert findMedian(arr) == 3

def test_findMedian_negative_numbers():
    arr = [-5, -3, -1, -2, -4]
    assert findMedian(arr) == -3

def test_findMedian_mixed_numbers():
    arr = [-5, 0, 10, -3, 7]
    assert findMedian(arr) == 0

def test_findMedian_single_element():
    arr = [42]
    assert findMedian(arr) == 42

def test_findMedian_duplicate_elements():
    arr = [3, 3, 5, 2, 1]
    assert findMedian(arr) == 3
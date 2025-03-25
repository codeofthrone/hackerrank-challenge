import pytest
from preparation_kit_python.DivisibleSumPairs import divisibleSumPairs

def test_divisible_sum_pairs_example_case():
    assert divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]) == 5

def test_divisible_sum_pairs_all_pairs():
    assert divisibleSumPairs(4, 1, [1, 2, 3, 4]) == 6

def test_divisible_sum_pairs_with_zeros():
    assert divisibleSumPairs(4, 2, [0, 2, 4, 6]) == 6

def test_divisible_sum_pairs_same_numbers():
    assert divisibleSumPairs(3, 3, [3, 3, 3]) == 3

def test_divisible_sum_pairs_large_k():
    assert divisibleSumPairs(5, 10, [1, 2, 3, 4, 5]) == 0


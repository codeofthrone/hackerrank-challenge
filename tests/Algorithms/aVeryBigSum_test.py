import sys
import os
import pytest
from Algorithms.aVeryBigSum import aVeryBigSum

# Add parent directory to path to import the module
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def test_aVeryBigSum_simple():
    assert aVeryBigSum([1, 2, 3, 4, 5]) == 15

def test_aVeryBigSum_with_large_numbers():
    assert aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 5000000015

def test_aVeryBigSum_with_single_number():
    assert aVeryBigSum([1000000000]) == 1000000000

def test_aVeryBigSum_with_empty_array():
    assert aVeryBigSum([]) == 0

def test_aVeryBigSum_with_negative_numbers():
    assert aVeryBigSum([-1, -2, -3, -4, -5]) == -15

def test_aVeryBigSum_with_mixed_numbers():
    assert aVeryBigSum([-1000000000, 1000000000, -1000000000, 1000000000]) == 0
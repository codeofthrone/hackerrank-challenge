import pytest
from preparation_kit_python.SparseArrays import SparseArrays

def test_sparseArrays_example_case():
    strings = ["ab", "ab", "abc"]
    queries = ["ab", "abc", "bc"]
    assert SparseArrays(strings, queries) == [2, 1, 0]

def test_sparseArrays_no_matches():
    strings = ["def", "ghi", "jkl"]
    queries = ["abc", "mno", "pqr"]
    assert SparseArrays(strings, queries) == [0, 0, 0]

def test_sparseArrays_all_matches():
    strings = ["abc", "abc", "abc"]
    queries = ["abc"]
    assert SparseArrays(strings, queries) == [3]

def test_sparseArrays_empty_strings():
    strings = ["", "", "abc"]
    queries = ["", "abc"]
    assert SparseArrays(strings, queries) == [2, 1]

def test_sparseArrays_case_sensitivity():
    strings = ["abc", "ABC", "Abc"]
    queries = ["abc", "ABC", "Abc", "abC"]
    assert SparseArrays(strings, queries) == [1, 1, 1, 0]
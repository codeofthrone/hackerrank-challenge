import pytest
from preparation_kit_python.example import add

def test_add():
    assert add(2, 3) == 5  # 測試 add(2,3) 是否回傳 5

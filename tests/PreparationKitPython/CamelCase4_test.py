import pytest 
from io import StringIO
import sys
import os
from unittest import mock

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from preparation_kit_python.CamelCase4 import CamelCase4

# Use pytest fixtures instead of unittest setup/teardown
@pytest.fixture
def stdin_mock():
    held = sys.stdin
    sys.stdin = StringIO()
    yield sys.stdin
    sys.stdin = held

# Convert test methods to pytest style
def test_split_method(stdin_mock):
    stdin_mock.write("S;M;plasticCup()")
    stdin_mock.seek(0)
    expected_output = "plastic cup\n"
    with StringIO() as buf, mock.patch('sys.stdout', new=buf):
        CamelCase4()
        assert buf.getvalue() == expected_output

def test_split_class(stdin_mock):
    stdin_mock.write("S;C;PlasticCup")
    stdin_mock.seek(0)
    expected_output = "plastic cup\n"
    with StringIO() as buf, mock.patch('sys.stdout', new=buf):
        CamelCase4()
        assert buf.getvalue() == expected_output

def test_split_variable(stdin_mock):
    stdin_mock.write("S;V;plasticCup")
    stdin_mock.seek(0)
    expected_output = "plastic cup\n"
    with StringIO() as buf, mock.patch('sys.stdout', new=buf):
        CamelCase4()
        assert buf.getvalue() == expected_output

def test_combine_method(stdin_mock):
    stdin_mock.write("C;M;plastic cup")
    stdin_mock.seek(0)
    expected_output = "plasticCup()\n"
    with StringIO() as buf, mock.patch('sys.stdout', new=buf):
        CamelCase4()
        assert buf.getvalue() == expected_output

def test_combine_class(stdin_mock):
    stdin_mock.write("C;C;plastic cup")
    stdin_mock.seek(0)
    expected_output = "PlasticCup\n"
    with StringIO() as buf, mock.patch('sys.stdout', new=buf):
        CamelCase4()
        assert buf.getvalue() == expected_output

def test_combine_variable(stdin_mock):
    stdin_mock.write("C;V;plastic cup")
    stdin_mock.seek(0)
    expected_output = "plasticCup\n"
    with StringIO() as buf, mock.patch('sys.stdout', new=buf):
        CamelCase4()
        assert buf.getvalue() == expected_output
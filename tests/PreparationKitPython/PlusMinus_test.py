import unittest
from io import StringIO
import sys
import os

# Add the parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from preparation_kit_python.PlusMinus import plusMinus

class TestPlusMinus(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        self.held_output.close()
        sys.stdout = sys.__stdout__

    def test_example_case(self):
        plusMinus([1, 1, 0, -1, -1])
        self.assertEqual(self.held_output.getvalue(), "0.400000\n0.400000\n0.200000\n")

    def test_all_positive(self):
        plusMinus([1, 2, 3, 4, 5])
        self.assertEqual(self.held_output.getvalue(), "1.000000\n0.000000\n0.000000\n")

    def test_all_negative(self):
        plusMinus([-1, -2, -3, -4, -5])
        self.assertEqual(self.held_output.getvalue(), "0.000000\n1.000000\n0.000000\n")

    def test_all_zeros(self):
        plusMinus([0, 0, 0, 0, 0])
        self.assertEqual(self.held_output.getvalue(), "0.000000\n0.000000\n1.000000\n")

    def test_mixed_elements(self):
        plusMinus([1, -1, 0, 1, -1, 0])
        self.assertEqual(self.held_output.getvalue(), "0.333333\n0.333333\n0.333333\n")
    def test_single_positive(self):
        plusMinus([1])
        self.assertEqual(self.held_output.getvalue(), "1.000000\n0.000000\n0.000000\n")

    def test_single_negative(self):
        plusMinus([-1])
        self.assertEqual(self.held_output.getvalue(), "0.000000\n1.000000\n0.000000\n")

    def test_single_zero(self):
        plusMinus([0])
        self.assertEqual(self.held_output.getvalue(), "0.000000\n0.000000\n1.000000\n")

    def test_large_numbers(self):
        plusMinus([1000000, -1000000, 0])
        self.assertEqual(self.held_output.getvalue(), "0.333333\n0.333333\n0.333333\n")

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            plusMinus([])
if __name__ == '__main__':
    unittest.main()
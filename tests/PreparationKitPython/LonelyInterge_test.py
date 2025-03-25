import unittest
import sys
import os

# Add the parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from preparation_kit_python.LonelyInterge import lonelyinteger

class TestLonelyInteger(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(lonelyinteger([1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(lonelyinteger([1, 1, 2]), 2)
        self.assertEqual(lonelyinteger([0, 0, 1, 2, 1]), 2)
        self.assertEqual(lonelyinteger([4, 9, 95, 93, 57, 4, 57, 93, 9]), 95)

    def test_negative_elements(self):
        self.assertEqual(lonelyinteger([-1, -1, -2]), -2)
        self.assertEqual(lonelyinteger([-3, -3, -4, -4, -5]), -5)

    def test_mixed_elements(self):
        self.assertEqual(lonelyinteger([1, -1, 1]), -1)
        self.assertEqual(lonelyinteger([0, 1, 2, 1, 2]), 0)

if __name__ == '__main__':
    unittest.main()
import unittest
from preparation_kit_python.TimeConversion import timeConversion

class TestTimeConversion(unittest.TestCase):
    def test_midnight(self):
        self.assertEqual(timeConversion("12:00:00AM"), "00:00:00")
        self.assertEqual(timeConversion("12:30:00AM"), "00:30:00")

    def test_noon(self):
        self.assertEqual(timeConversion("12:00:00PM"), "12:00:00")
        self.assertEqual(timeConversion("12:30:00PM"), "12:30:00")

    def test_am_times(self):
        self.assertEqual(timeConversion("01:00:00AM"), "01:00:00")
        self.assertEqual(timeConversion("11:59:59AM"), "11:59:59")

    def test_pm_times(self):
        self.assertEqual(timeConversion("01:00:00PM"), "13:00:00")
        self.assertEqual(timeConversion("11:59:59PM"), "23:59:59")

if __name__ == '__main__':
    unittest.main()
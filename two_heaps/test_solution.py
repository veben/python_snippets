import unittest
from solution import MedianFinder


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.medianFinder = MedianFinder()

    def test_first_case(self):
        self.medianFinder.addNum(1)
        self.medianFinder.addNum(2)
        expected = 1.5
        result = self.medianFinder.findMedian()
        self.assertEqual(result, expected)

    def test_second_case(self):
        self.medianFinder.addNum(1)
        self.medianFinder.addNum(2)
        self.medianFinder.addNum(3)
        expected = 2.0
        result = self.medianFinder.findMedian()
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

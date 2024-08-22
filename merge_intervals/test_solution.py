import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first_intervals(self):
        input = [[1,4],[4,5]]
        expected = [[1, 5]]
        result = self.solution.merge(input)
        self.assertEqual(expected, result)

    def test_second_intervals(self):
        input = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        result = self.solution.merge(input)
        self.assertEqual(expected, result)

    def test_third_intervals(self):
        input = [[1, 8], [2, 6], [8, 10]]
        expected = [[1, 10]]
        result = self.solution.merge(input)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()

import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first_case(self):
        input = [1, 2, 3]
        expected = sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
        result = sorted(self.solution.subsets(input))
        self.assertEqual(result, expected)

    def test_second_case(self):
        input = [0]
        expected = sorted([[], [0]])
        result = sorted(self.solution.subsets(input))
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

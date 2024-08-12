import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_value_error(self):
        colors = [1, 1]
        with self.assertRaises(ValueError):
            self.solution.number_of_alternating_groups(colors)

    def test_single_color(self):
        colors = [1, 1, 1]
        expected = 0
        result = self.solution.number_of_alternating_groups(colors)
        self.assertEqual(result, expected)

    def test_alternating_colors(self):
        colors = [0, 1, 0, 0, 1]
        expected = 3
        result = self.solution.number_of_alternating_groups(colors)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

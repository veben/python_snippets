import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first_matrix(self):
        input_matrix, k = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4
        expected = False
        result = self.solution.areSimilar(input_matrix, k)
        self.assertEqual(result, expected)

    def test_second_matrix(self):
        input_matrix, k = [[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], 2
        expected = True
        result = self.solution.areSimilar(input_matrix, k)
        self.assertEqual(result, expected)

    def test_third_matrix(self):
        input_matrix, k = [[2, 2], [2, 2]], 2
        expected = True
        result = self.solution.areSimilar(input_matrix, k)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

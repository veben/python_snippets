import unittest
from solution import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first_case(self):
        input = TreeNode(
            3, TreeNode(9, None, None), TreeNode(20, TreeNode(15), TreeNode(7))
        )
        expected = [[3], [9, 20], [15, 7]]
        result = self.solution.levelOrder(input)
        self.assertEqual(result, expected)

    def test_second_case(self):
        input = TreeNode(1)
        expected = [[1]]
        result = self.solution.levelOrder(input)
        self.assertEqual(result, expected)

    def test_third_case(self):
        input = None
        expected = []
        result = self.solution.levelOrder(input)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

import unittest
from solution import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first_case(self):
        input = TreeNode(
            5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
            TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
        )
        target_sum = 22
        expected = True
        result = self.solution.hasPathSum(input, target_sum)
        self.assertEqual(result, expected)

    def test_second_case(self):
        input = TreeNode(1, TreeNode(2), TreeNode(3))
        target_sum = 5
        expected = False
        result = self.solution.hasPathSum(input, target_sum)
        self.assertEqual(result, expected)

    def test_third_case(self):
        input = None
        target_sum = 0
        expected = False
        result = self.solution.hasPathSum(input, target_sum)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

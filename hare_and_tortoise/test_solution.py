import unittest
from solution import Solution, create_list_node_with_cycle


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first_case(self):
        head = create_list_node_with_cycle([3, 2, 0, -4], 1)
        expected = True
        result = self.solution.hasCycle(head)
        self.assertEqual(result, expected)

    def test_second_case(self):
        head = create_list_node_with_cycle([1, 2], 0)
        expected = True
        result = self.solution.hasCycle(head)
        self.assertEqual(result, expected)

    def test_third_case(self):
        head = create_list_node_with_cycle([1], -1)
        expected = False
        result = self.solution.hasCycle(head)
        self.assertEqual(result, expected)

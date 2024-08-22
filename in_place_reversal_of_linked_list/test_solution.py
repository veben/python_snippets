import unittest
from solution import Solution, ListNode


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first_list(self):
        input = [1, 2, 3, 4, 5]
        input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

        expected = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
        result = self.solution.reverseList(input)
        self.assertEqual(result, expected)

    def test_second_list(self):
        input = ListNode(1, ListNode(2))
        expected = ListNode(2, ListNode(1))
        result = self.solution.reverseList(input)
        self.assertEqual(result, expected)

    def test_third_list(self):
        input = ListNode(None)
        expected = ListNode(None)
        result = self.solution.reverseList(input)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

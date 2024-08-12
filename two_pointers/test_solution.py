import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_flip_and_invert_row(self):
        row = [1, 1, 0]
        expected = [1, 0, 0]
        result = self.solution.flip_and_invert_row(row)
        self.assertEqual(result, expected)

    def test_flip_and_invert_image(self):
        image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
        expected = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
        result = self.solution.flip_and_invert_image(image)
        self.assertEqual(result, expected)

    def test_flip_and_invert_image_with_second_image(self):
        image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
        expected = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
        result = self.solution.flip_and_invert_image(image)
        self.assertEqual(result, expected)

    def test_flip_and_invert_image2(self):
        image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
        expected = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
        result = self.solution.flip_and_invert_image_2(image)
        self.assertEqual(result, expected)

    def test_flip_and_invert_image2_with_second_image(self):
        image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
        expected = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
        result = self.solution.flip_and_invert_image_2(image)
        self.assertEqual(result, expected)

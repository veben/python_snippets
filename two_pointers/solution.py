from typing import List


class Solution:
    def flip_and_invert_row(self, row: List[int]) -> List[int]:
        left, right = 0, len(row) - 1
        while left <= right:
            row[left], row[right] = abs(row[right] - 1), abs(row[left] - 1)
            left += 1
            right -= 1
        return row

    def flip_and_invert_image(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = self.flip_and_invert_row(image[i])
        return image

    def flip_and_invert_image_2(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in image:
            i.reverse()  # reverse method return None but reverse the list
            res.append([x ^ 1 for x in i])  # x ^ 1 is a XOR
        return res

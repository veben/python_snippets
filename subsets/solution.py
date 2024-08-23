from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int, current: List[int]):
            result.append(current[:])
            for i in range(start, len(nums)):
                backtrack(i + 1, current + [nums[i]])

        result = []
        backtrack(0, [])
        return result

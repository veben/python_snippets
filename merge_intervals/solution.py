from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        intervals.sort(key=lambda x:x[0])

        tmp = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= tmp[1]:
                tmp[1] = max(interval[1], tmp[1])
            else:
                merged.append(tmp)
                tmp = interval

        merged.append(tmp)

        return merged
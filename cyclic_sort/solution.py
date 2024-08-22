from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k = k % n

        answer = []
        for i, row in enumerate(mat):
            if i % 2 == 0:
                answer.append(row[k:] + row[:k])
            else:
                answer.append(row[-k:] + row[:-k])

        return answer == mat

        # Can be written like that
        # return all(
        #     row == row[k:] + row[:k] if i % 2 == 0 else row == row[-k:] + row[:-k]
        #     for i, row in enumerate(mat)
        # )

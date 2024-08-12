from typing import List


class Solution:
    def number_of_alternating_groups(self, colors: List[int]) -> int:
        nb_colors = len(colors)

        if nb_colors < 3 or nb_colors > 100:
            raise ValueError("The number of colors should be between 3 and 100")

        sum = 0

        for i in range(nb_colors - 2):
            if colors[i] != colors[i + 1] and colors[i] == colors[i + 2]:
                sum += 1

        if colors[0] != colors[nb_colors - 1] and colors[0] == colors[nb_colors - 2]:
            sum +=1

        if colors[nb_colors - 1] != colors[0] and colors[nb_colors - 1] == colors[1]:
            sum +=1

        return sum

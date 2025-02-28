from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        ratings = [-1] + ratings + [-1]
        candies = [0] * len(ratings)
        for i in range(1, len(ratings)-1):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
            elif ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                candies[i] = 1
        for i in range(len(ratings)-2, 0, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)
import collections
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        counter = collections.Counter(position)
        # odds = [x for x in counter if x % 2 == 1]
        totalOdds = sum([counter[x] for x in counter if x % 2 == 1])
        # evens = [x for x in counter if x % 2 == 0]
        totalEvens = sum([counter[x] for x in counter if x % 2 == 0])

        # move to 1 or move to 99
        # move to 2 or move to 100
        return min(totalEvens, totalOdds)

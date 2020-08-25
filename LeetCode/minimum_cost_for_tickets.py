from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        minCost = [0] + [float('inf')] * days[-1]

        for d in range(1, days[-1] + 1):
            if d in days:
                if d > 30:
                    minCost[d] = min(minCost[d-1] + costs[0], minCost[d-6] + costs[1], minCost[d-29] + costs[2])
                elif  7 < d <= 30:
                    minCost[d] = min(minCost[d-1] + costs[0], minCost[d-6] + costs[1], minCost[0] + costs[2])
                else:
                    minCost[d] = min(minCost[d-1] + costs[0], minCost[0] + costs[1])
            else:
                minCost[d] = minCost[d-1]
        print(minCost)
        return minCost[-1]


if __name__ == '__main__':
    # days = [1,4,6,7,8,20]
    # days = [1,2,3,4,5,6,7,8,9,10,30,31]
    days = [1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28]
    # costs = [2, 7, 15]
    costs = [3, 13, 45]
    s = Solution()
    s.mincostTickets(days, costs)
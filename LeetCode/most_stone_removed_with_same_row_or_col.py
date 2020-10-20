# Union-Find Algorithm
from typing import List
from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # graph = defaultdict(list)
        parents = [i for i in range(len(stones))]
        n = len(stones)

        def find(x: int):
            if x == parents[x]:
                return x
            root = find(parents[x])
            parents[x] = root
            return root

        for i in range(n - 1):
            for j in range(i + 1, n):
                u = find(i)
                v = find(j)
                if u != v:
                    if stones[j][0] == stones[i][0] or stones[j][1] == stones[i][1]:
                        parents[v] = u

        answers = [i for i in range(n) if i == parents[i]]

        return len(stones) - len(answers)


if __name__ == '__main__':
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    print(Solution().removeStones(stones))

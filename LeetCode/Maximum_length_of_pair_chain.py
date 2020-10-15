from typing import List
from collections import defaultdict


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        graph = defaultdict(list)
        answer = 0
        visited = []
        for pair in pairs:
            graph[pair[0]].append(pair[1])

        def dfs(st: int, count: int):
            nonlocal answer
            if st not in graph:
                return
            for next in graph[st]:
                if next not in visited:
                    visited.append(next)
                    count += 1
                    dfs(next, count)
            answer = max(answer, count)

        for i in range(1, n + 1):
            if i not in visited:
                dfs(i, 0)
        print(answer - 1)
        return 0


if __name__ == '__main__':
    # pairs = [[1,2], [2,3], [3,4]]
    # pairs = [[1,2], [2,3], [3,4], [5, 6], [6, 7], [6, 8], [8, 9], [9, 10]]
    pairs = [[-10, -8], [8, 9], [-5, 0], [6, 10], [-6, -4], [1, 7], [9, 10], [-4, 7]]
    pairs.sort(key=lambda x: x[0])
    dp = defaultdict(int)
    dp[pairs[0][1]] = 1
    answer = 0
    for i in range(1, len(pairs)):
        temp = [x for x in dp if x < pairs[i][0]]
        if len(temp) > 0:
            for t in temp:
                dp[pairs[i][1]] = max(dp[pairs[i][1]], dp[t] + 1)
        else:
            dp[pairs[i][1]] = 1
        answer = max(answer, dp[pairs[i][1]])
    print(answer)
    # sol = Solution()
    # sol.findLongestChain(pairs)

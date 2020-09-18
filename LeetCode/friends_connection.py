from typing import List
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # Union-Find 풀이
        parents = [i for i in range(len(M) + 1)]
        n = len(M)

        def find(x: int):
            if x == parents[x]:
                return x
            p = find(parents[x])
            parents[x] = p
            return p

        for r in range(n):
            for c in range(r, n):
                if r != c and M[r][c] == 1:
                    u = find(r + 1)
                    v = find(c + 1)
                    if u != v:
                        parents[v] = u
        answer = [parent for index, parent in enumerate(parents) if index == parent and index > 0]
        return len(answer)
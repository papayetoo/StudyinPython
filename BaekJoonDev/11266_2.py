# 단절점 찾기 - articulation point
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 9)


class Solution:
    def findArticulationPoint(self):
        v, e = map(int, sys.stdin.readline().split())
        graph = defaultdict(list)
        # 무방향 그래프 생성
        for _ in range(e):
            u, w = map(int, sys.stdin.readline().split())
            graph[u].append(w)
            graph[w].append(u)

        dfn = [None] * (v + 1)
        low = [None] * (v + 1)
        ap = [False] * (v + 1)
        count = 0

        def dfs(node: int, count: int):
            nonlocal dfn, ap
            dfn[node] = low[node] = count
            children = 0
            ret = dfn[node]

            for nextNode in graph[node]:
                if dfn[nextNode] is not None:
                    ret = min(ret, dfn[nextNode])
                else:
                    children += 1
                    subtree = dfs(nextNode, count + 1)
                    if count != 1 and subtree >= dfn[node]:
                        ap[node] = True
                    ret = min(ret, subtree)

            if count == 1 and children >= 2:
                ap[node] = True

            return ret

        for i in range(1, v+1):
            if not dfn[i]:
                dfs(i, 1)
        answer = [i for i, ap in enumerate(ap) if i > 0 and ap]
        print(len(answer))
        print(*answer)


if __name__ == '__main__':
    sol = Solution()
    sol.findArticulationPoint()

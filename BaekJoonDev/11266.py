import sys
from collections import defaultdict


class Solution:
    def __init__(self, nVertex: int):
        # order[노드번호] = 방문순서
        self.nVertex = nVertex
        self.dfn = [0] * (nVertex + 1)
        self.low = [float('inf')] * (nVertex + 1)
        self.count = 1
        self.answer = set()

    def dfs(self, adj: defaultdict, visited: list, u: int):
        visited.append(u)
        self.dfn[u] = self.low[u] = self.count

        for v in adj[u]:
            if v not in visited:
                self.count += 1
                self.dfs(adj, visited, v)
                if self.dfn[u] <= self.low[v]:
                    self.answer.add(u)
                self.low[u] = min(self.low[u], self.low[v])
            else:
                self.low[u] = min(self.low[u], self.dfn[v])

    # def findConnectedComponent(self, adj: defaultdict, node: int, isRoot: bool):
    #     if isRoot and len(adjList[node]) >= 2:
    #         self.answer.append(node)
    #         return
    #     elif not isRoot:
    #         # 늦은 dfs 탐색번호 갖는 자식노드만 추출.
    #         lateNodes = [x for x in adj[node] if self.dfn[node] < self.dfn[x]]
    #         for i in lateNodes:
    #             if self.dfn[node] <= self.low[i]:
    #                 self.answer.append(node)
    #                 return
    #             else:
    #                 continue


if __name__ == '__main__':
    numOfVertex, numOfEdge = map(int, input().strip().split())
    adjList = defaultdict(list)
    for _ in range(numOfEdge):
        u, v = map(int, sys.stdin.readline().strip().split())
        adjList[u].append(v)
        adjList[v].append(u)
    s = Solution(numOfVertex)
    s.dfs(adjList, [], 1)
    answer = list(s.answer)
    answer.sort()
    print(len(answer))
    print(*answer)

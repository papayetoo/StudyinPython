import sys
from collections import defaultdict


class Solution:
    def __init__(self, nVertex: int):
        # order[노드번호] = 방문순서
        self.nVertex = nVertex
        self.dfn = [0] * (nVertex + 1)
        self.low = [float('inf')] * (nVertex + 1)
        self.count = 1
        self.answer = []

    def dfs(self, adj: defaultdict, visited: list, node: int):
        visited.append(node)
        self.dfn[node] = self.low[node] = self.count

        for next in adj[node]:
            print(node, next)
            if next not in visited:
                self.count += 1
                self.dfs(adj, visited, next)
            self.low[node] = min(self.low[node], self.dfn[next])

    def findConnectedComponent(self, adj: defaultdict, node: int, isRoot: bool):
        if isRoot and len(adjList[node]) >= 2:
            self.answer.append(node)
            return
        elif not isRoot:
            # 늦은 dfs 탐색번호 갖는 자식노드만 추출.
            lateNodes = [x for x in adj[node] if self.dfn[node] < self.dfn[x]]
            for i in lateNodes:
                if self.dfn[node] <= self.low[i]:
                    self.answer.append(node)
                    return
                else:
                    continue


if __name__ == '__main__':
    numOfVertex, numOfEdge = map(int, input().strip().split())
    adjList = defaultdict(list)
    for _ in range(numOfEdge):
        u, v = map(int, sys.stdin.readline().strip().split())
        adjList[u].append(v)
        adjList[v].append(u)
    s = Solution(numOfVertex)
    s.dfs(adjList, [], 1)
    for i in range(1, numOfVertex + 1):
        s.findConnectedComponent(adjList, i, True if i == 1 else False)
    print('dfn', s.dfn)
    print('low', s.low)
    print(len(s.answer))
    print(*s.answer)

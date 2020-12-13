# 그래프 탐색 DFS 와 BFS
import sys
from collections import defaultdict, deque
import bisect

input = sys.stdin


class Solution:
    @classmethod
    def dfs(cls, curr, graph, visited):
        arr = [curr]
        for nextNode in graph[curr]:
            if nextNode not in visited:
                visited.append(nextNode)
                arr += Solution.dfs(nextNode, graph, visited)
        return arr

    @classmethod
    def bfs(cls, curr, graph):
        answer = [curr]
        q = deque([curr])
        while q:
            front = q.popleft()
            for nextNode in graph[front]:
                if nextNode not in answer:
                    answer.append(nextNode)
                    q.append(nextNode)
        return answer


if __name__ == "__main__":
    vertex, edges, st = map(int, input.readline().split())
    graph = defaultdict(list)
    for _ in range(edges):
        u, v = map(int, input.readline().split())
        posU = bisect.bisect_left(graph[u], v)
        graph[u].insert(posU, v)
        posV = bisect.bisect_left(graph[v], u)
        graph[v].insert(posV, u)
    print(*Solution.dfs(st, graph, [st]))
    print(*Solution.bfs(st, graph))

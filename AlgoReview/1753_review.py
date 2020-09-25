from heapq import heappop, heappush
from collections import defaultdict


class Solution:
    def dijkstra(self, v: int, st: int, adj: defaultdict) -> [int]:
        dist = [float('inf')] * (v + 1)
        dist[st] = 0
        queue = [(0, st)]
        while queue:
            weight, to_next = heappop(queue)
            for (value, index) in adj[to_next]:
                if dist[index] > weight + value:
                    heappush(queue, (weight+value, index))
                    dist[index] = weight + value

        for i in range(1, len(dist)):
                print(dist[i] if dist[i] != float('inf') else 'INF')
        return dist


if __name__ == '__main__':
    numOfVertex, numOfEdge = map(int, input().split())
    st = int(input())
    adjList = defaultdict(list)
    for _ in range(numOfEdge):
        u, v, cost = map(int, input().split())
        adjList[u].append((cost, v))
        # adjList[v].append((cost, u))
    s = Solution()
    s.dijkstra(numOfVertex, st, adjList)
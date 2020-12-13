from collections import defaultdict
import sys
import heapq

input = sys.stdin


class Solution:
    @classmethod
    def dijkstra(cls, n, st, end, graph):
        dist = [float('inf') for _ in range(n + 1)]
        before = [None for _ in range(n+1)]
        dist[st] = 0
        q = []
        heapq.heappush(q, [0, st])
        while q:
            (d, mid) = heapq.heappop(q)
            for cost, e in graph[mid]:
                if dist[e] > d + cost:
                    dist[e] = d + cost
                    before[e] = mid
                    heapq.heappush(q, (d+cost, e))
        print(dist[end])
        curr = end
        path = []
        while curr is not None:
            path.append(curr)
            curr = before[curr]
        print(len(path))
        print(*path[::-1])


if __name__ == "__main__":
    n = int(input.readline())
    bus = int(input.readline())
    graph = {x: [] for x in range(1, n + 1)}

    for _ in range(bus):
        u, v, cost = map(int, input.readline().split())
        heapq.heappush(graph[u], (cost, v))
    st, end = map(int, input.readline().split())
    # q = [(-cost, index) for index, cost in enumerate(graph[st]) if index > 0]
    # q = []
    # for index in range(1, n+1):
    #     heapq.heappush(q, (graph[st][index], index))
    # Solution.dijkstra(n, st, end, q, graph)
    Solution.dijkstra(n, st, end, graph)

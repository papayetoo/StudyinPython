import sys
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def dijkstra(self, v: int, st: int, end: int, adj: defaultdict):
        dist = [10**12 for _ in range(v + 1)]
        dist[st] = 0
        queue = [(0, st)]
        path = [[] for _ in range(v + 1)]

        while queue:
            midCost, nextCity = heappop(queue)
            for (endCost, endCity) in adj[nextCity]:
                if dist[endCity] >= midCost + endCost:
                    path[endCity].append(nextCity)
                    heappush(queue, (midCost + endCost, endCity))
                    dist[endCity] = midCost + endCost
        print(dist[end])
        print(len(path[end]) + 1)
        print(*path[end], end)


if __name__ == '__main__':
    s = Solution()
    numOfCity = int(input())
    numOfBus = int(input())
    adjList = defaultdict(list)
    for _ in range(numOfBus):
        startCity, endCity, busCost = map(int, sys.stdin.readline().split())
        adjList[startCity].append((busCost, endCity))
    startCity, endCity = map(int, sys.stdin.readline().split())
    s.dijkstra(numOfCity, startCity, endCity, adjList)
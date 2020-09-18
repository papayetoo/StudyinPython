from typing import List
from collections import defaultdict
from collections import deque
import bisect
import heapq


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union-Find 사용해서 문제해결
        parents = [i for i in range(len(edges) + 1)]

        def find(node: int):
            if node == parents[node]:
                return node
            root = find(parents[node])
            parents[node] = root
            return root

        answer = []
        for edge in edges:
            u = find(edge[0])
            v = find(edge[1])
            if u != v:
                parents[v] = u
            else:
                answer.append(edge[0])
                answer.append(edge[1])

        return answer

    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
        visited = []
        graph = defaultdict(list)
        e = [i + 1 for i in range(len(edges) + 1)]
        stack = deque()

        for edge in edges:
            u = edge[0]
            v = edge[1]
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node: int):
            stack.append(node)
            while stack:
                current = stack.pop()
                for next in graph[current]:
                    if next not in visited:
                        visited.append(next)
                visited.append(current)

        for edge in edges:
            u = edge[0]
            dfs(u)
        print(visited)

    def findCycle(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for (u, v) in edges:
            graph[u].insert(bisect.bisect_left(graph[u], v), v)
            graph[v].insert(bisect.bisect_left(graph[v], u), u)
        visited = []
        loop = []

        def dfs(node: int):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    dfs(neighbor)
                    loop.append([min(node, neighbor), max(node, neighbor)])

        for u in graph:
            print(u)
            if u not in visited:
                # visited[u] += 1
                dfs(u)
        # for (u, v) in edges:
        #     if u not in visited:
        #         dfs(u)
        print(loop)
        # duplicate = set([x for x in visited if visited.count(x) > 1])
        # answer = [e for e in edges if e[0] in duplicate or e[1] in duplicate]
        return []


if __name__ == '__main__':
    s = Solution()
    # arr = [[1, 2], [1, 3], [2, 3]]
    # arr = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
    # arr = [[5,2],[5,1],[3,1],[3,4],[3,5]]
    # arr = [[3,4],[1,2],[2,4],[3,5],[2,5]]
    arr = [[1,4],[3,4],[1,3],[1,2],[4,5]]
    # arr = [[1,2], [1, 3], [2, 3], [2, 4]]
    print(s.findCycle(arr))

from typing import List
from collections import defaultdict
from collections import deque
import bisect


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # edges.sort(key=lambda x: x[0])
        for edge in edges:
            u = edge[0]
            v = edge[1]
            # insertPos = bisect.bisect_left(graph[u], v)
            # graph[u].insert(insertPos, v)
            graph[u].append(v)

        visited = []

        def dfs(node: int):
            visited.append(node)
            for p in graph[node]:
                if p not in visited:
                    dfs(p)
                else:
                    print(node, p)

        def bfs(node: int):

            queue = deque()
            queue.append(node)

            while queue:
                front = queue.pop()
                visited.append(front)
                for elem in graph[front]:
                    if elem not in visited:
                        queue.append(elem)
                        visited.append(elem)
                    else:
                        return front, elem
            return None

        answer = []
        for edge in edges:
            print(edge)
            if edge[0] not in visited:
                result = bfs(edge[0])
                if result is not None:
                    print('test', result)

        return []


if __name__ == '__main__':
    s = Solution()
    # arr = [[5,2],[5,1],[3,1],[3,4],[3,5]]
    arr = [[2,1],[3,1],[4,2],[1,4]]
    s.findRedundantDirectedConnection(arr)


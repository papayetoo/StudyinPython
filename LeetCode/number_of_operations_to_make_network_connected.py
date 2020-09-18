from typing import List
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]):
        # Union-Find
        # n 은 노드의 개수
        parents = [i for i in range(n)]

        def find(x: int):
            if x ==  parents[x]:
                return x
            root = find(parents[x])
            parents[x] = root
            return root

        edgeCount = 0
        cycleEdgeCount = 0
        for (left, right) in connections:
            u = find(left)
            v = find(right)
            if u != v:
                parents[v] = u
                edgeCount += 1
            else:
                cycleEdgeCount += 1

        return n - 1 - edgeCount if n - 1 <= edgeCount + cycleEdgeCount else -1


if __name__ == '__main__':
    # Case 1
    n = 4
    connections = [[0,1], [0,2], [1,2]]
    # Case 2
    # n = 6
    # connections = [[0, 1], [0, 2], [0, 3], [1, 2], [4, 5]]
    # connections = [[0,1],[0,2],[0,3],[1,2]]
    # Case 3
    # n = 5
    # connections = [[0, 1], [0, 2], [3, 4], [2, 3]]
    # Wrong Answer
    # n = 12
    # connections = [[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]]
    s = Solution()
    print(s.makeConnected(n, connections))
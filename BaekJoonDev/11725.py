# BFS 부모 찾기 문제
import sys
from collections import defaultdict
from collections import deque


def find(x: int, parents: list):
    if x == parents[x]:
        return x
    root = find(parents[x], parents)
    parents[x] = root
    return root


def bfs(q: deque, gr: defaultdict, parents_lst: list):
    while (q):
        parent = q.popleft()
        for child in gr[parent]:
            if parents_lst[child] == float('inf'):
                parents_lst[child] = parent
                q.append(child)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    parents = [float('inf') for i in range(n + 1)]
    parents[1] = 0
    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().strip().split())
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([1])
    bfs(queue, graph, parents)
    for i in range(2, n+1):
        print(parents[i])

import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)

dfs_visited = []
def dfs(arr:[[int]], st:int):
    print(st + 1, end=' ')
    dfs_visited.append(st)
    for i in range(len(arr[st])):
        if arr[st][i] == 1 and i not in dfs_visited:
            dfs(arr, i)

bfs_visited = []
def bfs(arr:[[int]], st: int):

    q = deque()
    q.append(st)
    bfs_visited.append(st)

    while q:
        front = q.popleft()
        print(front+1, end=' ')
        for index, value in enumerate(arr[front]):
            if index not in bfs_visited and value == 1:
                q.append(index)
                bfs_visited.append(index)



if __name__ == '__main__':
    n, m, st = map(int, input().split())
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        arr[u-1][v-1] = 1
        arr[v-1][u-1] = 1

    dfs(arr, st - 1)
    print()
    bfs(arr, st - 1)

from copy import deepcopy


def bellman_ford(arr: [[int]], v: int, start: int):
    # 2D array version
    dist = [float('inf') for _ in range(v)]
    dist[start] = 0

    for counter in range(v):
        for a in range(v):
            print(dist)
            for b in range(v):
                if arr[a][b] != float('inf') and dist[a] != float('inf'):
                    dist[b] = min(dist[b], dist[a] + arr[a][b])


def bellman_ford_dict(edges, v: int, start: int):
    # 시작 배열 초기화
    dist = [float('inf') for _ in range(v)]
    dist[start] = 0

    for counter in range(v):
        for src in edges:
            print(dist)
            for dest in edges[src]:
                print(dest, dist[src])
                if dist[src] != float('inf') and dist[dest] > dist[src] + edges[src][dest]:
                    dist[dest] = dist[src] + edges[src][dest]


arr = [[0, -4, 5, 2, 3],
       [float('inf'), 0, float('inf'), -1, float('inf')],
       [float('inf'), float('inf'), 0, -7, float('inf')],
       [float('inf'), float('inf'), float('inf'), 0, 6],
       [float('inf'), float('inf'), float('inf'), -4, 0]
       ]
#
# V 5 E 8
# 0 1 -4
# 0 2 5
# 0 3 2
# 0 4 3
# 1 3 -1
# 2 3 -7
# 3 4 6
# 4 3 -4
edges = {0: {1: -4, 2: 5, 3: 2, 4: 3}, 1: {3: -1}, 2: {3: -7}, 3: {4: 6}, 4: {3: -4}}
bellman_ford(arr, 5, 0)
# bellman_ford_dict(edges, 5, 1)
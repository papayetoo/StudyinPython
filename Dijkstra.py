import collections, heapq
def dijkstra(times: [[]], N:int, K:int) -> int:
    """ 다익스트르라 구현"""
    g = collections.defaultdict(list)
    # 리스트 형태로 value를 저장할 수 있다는 의미.
    for u,v,cost in times:
        g[u].append((v, cost))

    min_heap = [(0, K)]
    distance = {}
    distance[K] = 0
    while min_heap:
        cost, cur = heapq.heappop(min_heap)
        distance[cur] = cost
        if len(distance) == N:
            break
        for neighbor, weight in g[cur]:
            if neighbor not in distance:
                heapq.heappush(min_heap, (cost + weight, neighbor))

    return max(distance.values()) if len(distance) == N else -1

def bellman_ford(times:[[]], N:int, K:int) -> int:
    """ 벨만 포드 구현"""
    dist = {i : float("inf") for i in range(1, N+ 1)}
    dist[K] = 0
    for _ in range(N-1):
        for u,v,w in times:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
        print(dist)
    return max(dist.values()) if max(dist.values()) != float("inf") else -1

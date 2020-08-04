import sys
from collections import defaultdict
from heapq import heappush, heappop


def solution(d: defaultdict(dict), st: int, n_node: int):
    visited = [st]
    dist = [float('inf')] * (n_node + 1)
    dist[st] = 0
    for key, value in d[st].items():
        dist[key] = value

    while True:
        # 최소값 찾는 과정
        min_val = 11
        min_idx = -1
        for idx, val in enumerate(dist):
            if idx not in visited and val < min_val :
                min_val = val
                min_idx = idx

        if min_idx == -1:
            return dist
        visited.append(min_idx)

        for to_index in d[min_idx].keys():
            dist[to_index] = min(dist[to_index], dist[min_idx] + d[min_idx][to_index])


def dijkstra(arr:list, start: int, n_node: int):
    # dist 초기화
    dist = [float('inf') for _ in range(n_node + 1)]
    dist[start] = 0
    # 최소힙이 python 기본임
    # 최소힙 값의 앞의 우선순위 낮은 게 가장 최상단으로 감.
    q = [(0, start)]
    while q:
        weight, to_index = heappop(q)
        for (index, value) in arr[to_index]:
            if dist[index] > weight + value:
                heappush(q, (weight+value, index))
                dist[index] = weight + value
    # 결과값 리턴
    return dist


if __name__ == '__main__':
    v, e = map(int, sys.stdin.readline().split())
    st = int(sys.stdin.readline())
    d = [[] for _ in range(v + 1)]
    for _ in range(e):
        s, e, w = map(int, sys.stdin.readline().split())
        d[s].append((e,w))

    answer = dijkstra(d, st, v)
    for a in answer[1:]:
        print(a if a != float('inf') else 'INF')


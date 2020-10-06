from collections import defaultdict
from copy import deepcopy
import heapq


def solution(arr: list, start: int):
    dist_arr = [float('inf')] * len(arr)
    dist_arr[start] = 0
    d = [(arr[start], start)]
    while d:
        weight, index = heapq.heappop(d)
        for to_dist, to_index in arr[index]:
            if dist_arr[to_index] > weight + to_dist:
                dist_arr[to_index] = weight + to_dist
                d.append((weight + to_dist, index))
    print(dist_arr)


if __name__ == '__main__':
    v, e = map(int, input().split())
    st = int(input())
    d = defaultdict(list)
    for _ in range(e):
        s, e, w = map(int, input().split())
        d[s].append((w, e))
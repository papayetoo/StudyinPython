from sys import stdin
from heapq import heappush, heappop
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
q = []

def init():
    for i in range(n):
        for j in range(n):
            if a[i][j] == 9:
                heappush(a, (0, i, j)) # (time, y, x)
                a[i][j] =0
                return

def bfs():
    body, eat, ans = 2, 0, 0
    check = [[False] * n for _ in range(n)]

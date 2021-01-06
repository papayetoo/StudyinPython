# 아기상어
import sys
import heapq
from collections import deque


def bfs(start : list, seas: list, current_size):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    y, x, dist = start
    q = deque([start])
    seas[y][x] = 0
    visited = set()
    eatingFishes = []

    while q:
        y, x, dist = q.popleft()
        visited.add((y, x))
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < len(seas) and 0 <= nx < len(seas) and (ny, nx) not in visited:
                visited.add((ny, nx))
                if seas[ny][nx] == 0  or seas[ny][nx] == current_size:
                    q.append((ny, nx, dist + 1))
                    continue
                if seas[ny][nx] > current_size:
                    continue
                else:
                    heapq.heappush(eatingFishes, (dist + 1, ny, nx))

    if eatingFishes:
        return eatingFishes[0]
    else:
        return None

if __name__ == "__main__":
    n = int(input())
    grid = [[] for _ in range(n)]
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        grid[i] = temp

    pos = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 9:
                pos = [i, j]
    current_size = 2
    already_eat = 0
    answer = 0
    while True:
        eatingFish = bfs((pos[0], pos[1], 0), grid, current_size)
        if eatingFish is None:
            break
        dist, y, x = eatingFish
        answer += dist
        already_eat += 1
        if already_eat == current_size:
            current_size += 1
            already_eat = 0

        pos = (y, x)
    print(answer)

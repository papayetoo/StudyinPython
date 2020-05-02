from sys import stdin
from itertools import combinations
from copy import deepcopy
from collections import deque
#  입력 받아 배열 저장 부
n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

# 바이러스의 위치 저장
viruspos = []
emptycount = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            viruspos.append((0, i, j))
        elif arr[i][j] == 0:
            emptycount += 1

visited = []
result = []
# 조합 생성 -- 시간 초과 해결방안 중의 1
comblst = list(combinations(viruspos, m))
ans = 1e9

def bfs(grid:[], lst):
    global ans
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    q = deque(lst) # 시간 초과 해결방안 2 우선순위 큐에서 일반 큐로 변
    infect = 0

    time = 0
    while q :

        t, y, x = q.popleft()

        for i in range(4):
            if 0 <= y + dy[i] < n and 0 <= x + dx[i] < n:
                if grid[y+dy[i]][x+dx[i]] == -1 and arr[y+dy[i]][x+dx[i]] != 1:
                    grid[y + dy[i]][x + dx[i]] = t + 1
                    q.append((t + 1, y+dy[i], x+dx[i]))
                    if arr[y+dy[i]][x+dx[i]] == 0:
                        time = grid[y + dy[i]][x + dx[i]]
                        infect += 1

    # for i in range(n):
    #     print(grid[i])

    if infect == emptycount:
        ans = min(ans, time)



def comb(index, cnt):

    if index > len(viruspos):
        return

    if cnt == 0:
        q = []
        global result
        for i in range(len(viruspos)):
            if i in visited:
                q.append((0,viruspos[i][1], viruspos[i][2]))
        copyarr = deepcopy(arr)
        bfs(copyarr, q)
        return

    visited.append(index)
    comb(index+1, cnt-1)
    visited.pop()
    comb(index+1, cnt)

# comb(0, m)

for index, value in enumerate(comblst):
    # dist = deepcopy(arr) 이부분이 느림의 원인.
    dist = [[-1] * n for _ in range(n)]
    for v in value:
        dist[v[1]][v[2]] = 0
    bfs(dist, value)

print(ans if ans != 1e9 else -1)


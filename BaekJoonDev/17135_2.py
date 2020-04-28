from itertools import combinations
from copy import deepcopy
from heapq import heappush, heappop

row, col, attack_dist = map(int, input().split())
enemies = [ list(map(int, input().split()) ) for _ in range(row) ]
zeros = [0] * col

def kill(e:list, archerPos):
    cnt = 0
    for _ in range(row):
        v = []
        for k in range(3):
            q = []
            for i in range(row):
                for j in range(col):
                    if e[i][j]:
                        dist = abs(row - i) + abs(archerPos[k] - j)
                        if attack_dist >= dist:
                            heappush(q, (dist, j, i))
            if q:
                _, y, x = heappop(q)
                v.append((x,y))

        for x, y in v:
            if e[x][y]:
                e[x][y] = 0
                cnt +=1

        for i in range(row-2, -1, -1):
                for j in range(col):
                    e[i+1][j] = e[i][j]
        e[0] = zeros
    return cnt

ans = 0
for i in range(col):
    for j in range(i+1, col):
        for k in range(j+1, col):
            copyEnemies = deepcopy(enemies)
            ans = max(ans, kill(copyEnemies, [i,j,k]))

print(ans)






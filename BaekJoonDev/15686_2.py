import sys
import numpy as np
import time

starttime = time.mktime(time.localtime())
sys.setrecursionlimit(10**9)
n, numMax = map(int, input().split())
arr = [ list( map(int, input().split()) ) for _ in range(n)]
homes = []
chicken = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            homes.append( (i, j))
        elif arr[i][j] == 2:
            chicken.append( (i, j))

# visited = np.zeros(len(chicken), dtype=int)
visited = []
dist = []
ans = 10**9
def chickenCombination(start, pickNum):
    global ans
    if start > len(chicken):
        return

    if pickNum == 0:
        ans = min(ans, calculateDistance())
        dist.append(calculateDistance())
        return

    # visited[start] = 1
    visited.append(start)
    chickenCombination(start+1, pickNum-1)
    visited.pop()
    chickenCombination(start+1, pickNum)

def calculateDistance():
    result = 0
    for h in homes :
        temp = 10**9
        # for i in range(len(visited)):
            # if visited[i] == 1:
            #     distance = abs(h[0] - chicken[i][0]) + abs(h[1] - chicken[i][1])
            #     temp = min(distance, temp)
        for v in visited:
            distance = abs(h[0] - chicken[v][0]) + abs(h[1] - chicken[v][1])
            temp = min(distance, temp)
        result += temp
    return result

chickenCombination(0, numMax)
print( ans)

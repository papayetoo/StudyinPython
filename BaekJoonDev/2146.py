# 백준 2146번 문제 _____ BFS or DFS
import sys, copy
islandCount = 2
visited = -1
sys.setrecursionlimit(10**8)
islandInfo = []
# island 정보를 저장하는 함수.
class island:
    y = 0
    x = 0
    islNum = 0
    def __init__(self, y, x, islNum):
        self.y = y
        self.x = x
        self.islNum = islNum

# 각 섬을 다른 색으로 칠하는 함수.
def dfs_island(islandMap = [[]], r = 0, c = 0):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(4):
        if r + dy[i] >= 0 and r + dy[i] < len(islandMap) and c + dx[i] >= 0 and c + dx[i] < len(islandMap) and islandMap[r+dy[i]][c+dx[i]] == 0 :
            islandMap[r][c] = -islandCount
        if r + dy[i] >= 0 and r + dy[i] < len(islandMap) and c + dx[i] >= 0 and c + dx[i] < len(islandMap) and islandMap[r+dy[i]][c+dx[i]] == 1 :
            islandMap[r+dy[i]][c+dx[i]] = islandCount
            dfs_island(islandMap, r + dy[i], c + dx[i])
            islandInfo.append(island(r + dy[i], c + dx[i], islandCount))

def min_bridge():
    answer = 100000
    while len(islandInfo) != 0 :
        island0 = islandInfo.pop()
        y0 = island0.y
        x0 = island0.x
        islNum0 = island0.islNum

        copyInfo = islandInfo
        while len(copyInfo) != 0 :
            island1 = copyInfo.pop()
            y1 = island1.y
            x1 = island1.x
            islNum1 = island1.islNum

            if islNum0 == islNum1:
                continue
            else:
                answer = min(answer, abs(y1 - y0) + abs(x1 - x0) - 1)
    return answer

# def shortest_bridge(list = [[]]):
#     for i in range(len(list)):
#         for j in range(len(list[i])):
#             if list[i][j] < 0:

n = int(input())
islandMap = [[] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
mapIn = []
for i in range(n):
    islandMap[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if islandMap[i][j] == 1:
            islandMap[i][j] = islandCount
            islandInfo.append(island(i,j, islandCount))
            dfs_island(islandMap, i, j)
            islandCount += 1
print(min_bridge())
# for i in range(n):
#     print(islandMap[i])
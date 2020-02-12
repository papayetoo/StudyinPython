# 백준 1389번 문제 ____ 플로이드-워셜 알고리즘
import sys, collections
n, m = map(int, input().split())
# n, m 입력 받음.
arr = [[10000 for _ in range(n)] for _ in range(n)]
# 이차원 배열 생성.

for _ in range(m):
    first, second = map(int, input().split())
    arr[first - 1][second - 1] = 1
    arr[second - 1][first - 1] = 1

def floyd_warshall(size, fwarr = [[]]):
    # 거쳐가는 노드
    for k in range(size):
        # 출발 노드
        for i in range(size):
                # 도착 노드
                for j in range(size):
                    if i != j :
                        fwarr[i][j] = min(fwarr[i][j], fwarr[i][k] + fwarr[k][j])

floyd_warshall(n, arr)
sumArr = [0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j :
            sumArr[i] += arr[i][j]
for i in range(n):
    print(arr[i])

minValue = min(sumArr)
minIndex = sumArr.index(minValue) + 1
print(minIndex)
# 백준 11055 문제 가장 긴 증가하는 부분 수열
# LIS 알고리즘의 응용
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
v = arr.copy()

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and v[i] < v[j] + arr[i]:
            v[i] = v[j] + arr[i]
print(max(v))
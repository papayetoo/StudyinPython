# 백준 14002번 문제 가장 긴 증가하는 부분 수열4
import sys, bisect
def lowerbound(arr=[], x = 0):
    result = -1
    for i in range(len(arr)):
        if arr[i] >= x:
            return i
    return result
def upperbound(arr = [], x = 0):
    result = -1
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] <= x:
            return i
    return result
n = int(input())
arr = list(map(int, input().split()))
v = [arr[0]]
ans = [(0, arr[0])]
j = 0
for i in range(1, n):
        if v[j] < arr[i]:
            v.append(arr[i])
            j += 1
            ans.append((j, arr[i]))
        else:
            # lIndex = lowerbound(v, arr[i])
            lIndex = bisect.bisect_left(v, arr[i])
            v[lIndex] = arr[i]
            ans.append((lIndex, arr[i]))

s = []
t = len(v) - 1
ans.reverse()
# for i in range(n - 1, -1, -1):
#     if ans[i][0] == t:
#         s.append(ans[i][1])
#         t -= 1
for i in range(n):
    if ans[i][0] == t:
        s.append(ans[i][1])
        t -= 1
print(len(v))
# while len(s) != 0:
#     print(s.pop(), end=' ')
print(*reversed(s))
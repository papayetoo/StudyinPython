# 온라인 판매
import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(m):
    arr.append(int(sys.stdin.readline()))
arr.sort(reverse=True)

profits = [arr[eggs] * (eggs + 1) for eggs in range(n)]
max_index = profits.index(max(profits))
print(arr[max_index], max(profits))

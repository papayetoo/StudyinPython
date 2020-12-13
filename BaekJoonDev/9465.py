# 다이나믹 프로그래밍 스티커
import sys

if __name__ == "__main__":
    t = int(input())
    answer = []
    for _ in range(t):
        cols = int(input())
        arr = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
        u = [0 for _ in range(cols)]
        d = [0 for _ in range(cols)]
        u[0] = arr[0][0]
        d[0] = arr[1][0]
        for i in range(1, cols):
            u[i] = max(d[i-1] + arr[0][i], max(u[i-2], d[i-2]) + arr[0][i] if i - 2 >= 0 else arr[0][i])
            d[i] = max(u[i-1] + arr[1][i], max(u[i-2], d[i-2]) + arr[1][i] if i - 2 >= 0 else arr[1][i])
        answer.append(max(u[-1], d[-1]))
    for ans in answer:
        print(ans)
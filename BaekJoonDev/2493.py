import sys

# 탑 문제 -> stack
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    stc = []
    answer = [0] * n
    for i in range(n-1, -1, -1):
        if not stc:
            stc.append(i)
            continue

        while stc and arr[i] >= arr[stc[-1]]:
            index = stc.pop()
            answer[index] = i + 1

        stc.append(i)
    while stc:
        index = stc.pop()
        answer[index] = 0

    print(*answer)


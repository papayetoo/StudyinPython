# 백준 14889번 스타트와 링크
import itertools
n = int(input())
numbers = [i + 1 for i in range(n)]
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

comblist = list(itertools.combinations(numbers, int(n/2)))
answer = 1000000
for i in range(int(len(comblist)/2)):
    j = len(comblist) - i - 1
    sumA = 0
    sumB = 0
    for first in comblist[i]:
        for second in comblist[i]:
            if first != second:
                sumA += arr[first - 1][second - 1]
    for first in comblist[j]:
        for second in comblist[j]:
            if first != second:
                sumB += arr[first - 1][second - 1]

    # for a in list(itertools.permutations(comblist[i],2)):
    #     first = a[0]
    #     second = a[1]
    #     sumA += arr[first - 1][second - 1]
    # for b in list(itertools.permutations(comblist[j], 2)):
    #     first = b[0]
    #     second = b[1]
    #     sumB += arr[first - 1][second - 1]
    if answer > abs(sumA - sumB):
        answer = abs(sumA - sumB)

print(answer)
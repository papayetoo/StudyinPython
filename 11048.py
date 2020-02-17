import copy
stdin = list(map(int,input().split()))
arr = [[] for _ in range(stdin[0])]
for row in range(stdin[0]):
    arr[row] = list(map(int, input().split()))

def solution(arr = [[]], row = 0, col = 0):
    answer = copy.deepcopy(arr)
    for i in range(row):
        for j in range(col):
            if i - 1 >= 0 and j -1 >= 0:
                answer[i][j] = max(answer[i - 1][j], answer[i][j-1], answer[i-1][j-1]) + arr[i][j]
            elif i - 1 >= 0 and j - 1 < 0:
                answer[i][j] = answer[i-1][j] + arr[i][j]
            elif i - 1 < 0 and j - 1 >= 0:
                answer[i][j] = answer[i][j - 1] + arr[i][j]
    return  answer

ans = solution(arr,stdin[0], stdin[1])
for i in range(stdin[0]):
    print(ans[i])
# print(ans[stdin[0] - 1][stdin[1] - 1])
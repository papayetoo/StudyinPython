
def solution(n):
    div = 10007
    dp = [[0] * 10 for i in range(1001)]
    for i in range(10):
        dp[1][i] = 1
    for i in range(2, 1001):
        for j in range(0, 10):
            dp[i][j] = sum(dp[i - 1][j:10]) % div
    return sum(dp[int(n)]) % div
n = input()
answer = solution(n)
print(answer)
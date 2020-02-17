sugar = int(input())
dp = [-1 for _ in range(0, 5001)]
dp[3] = 1
dp[5] = 1
def solution():
    for i in range(6, 5001):
        if dp[i - 3] != -1 and dp[i - 5] != -1:
            dp[i] = 1 + min(dp[i-3], dp[i-5])
        elif dp[i - 3] != -1 and dp[i - 5] == -1:
            dp[i] = 1 + dp[i - 3]
        elif dp[i - 3] == -1 and dp[i - 5] != -1:
            dp[i] = 1 + dp[i - 5]

solution()
print(dp[sugar])




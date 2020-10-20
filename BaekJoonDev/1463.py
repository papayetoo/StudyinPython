def makeOne(k: int):
    dp = [0 for _ in range(10**6 + 1)]
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1

    for i in range(4, k+1):
        if i % 3 == 0 and i % 2 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i // 2] + 1, dp[i-1] + 1)
        elif i % 3 == 0 and i % 2 != 0:
            dp[i] = min(dp[i // 3] + 1, dp[i-1] + 1)
        elif i % 2 == 0 and i % 3 != 0:
            dp[i] = min(dp[i // 2] + 1, dp[i-1] + 1)
        else:
            dp[i] = dp[i-1] + 1

    return dp[k]


if __name__ == "__main__":
    k = int(input())
    print(makeOne(k))
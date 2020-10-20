def deliverSugar(sugar: int):
    dp = [-1 for _ in range(5001)]
    dp[3] = 1
    dp[5] = 1

    for i in range(4, 5001):
        if dp[i-3] != -1 and dp[i-5] != -1:
            dp[i] = min(dp[i-5] + 1, dp[i-3] + 1)
        elif dp[i-3] != -1:
            dp[i] = dp[i-3] + 1
        elif dp[i-5] != -1:
            dp[i] = dp[i-5] + 1
    return dp[sugar]


if __name__ == "__main__":
    k = int(input())
    print(deliverSugar(k))
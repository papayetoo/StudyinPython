n = input()
dp = list(0 for i in range(91))
dp[1] = 1
dp[2] = 1

for i in range(3, 91):
    dp[i] = dp[i -1] + dp[i -2]

print(dp[int(n)])
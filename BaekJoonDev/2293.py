import itertools
n, k = input().split()
coins = []
for _ in range(int(n)):
    coins.append(int(input()))
coins.sort()
dp = [0 for _ in range(int(k) + 1)]
dp[0] = 1
for i in range(1,len(dp)):
    if i % coins[0] == 0:
        dp[i] = 1

for i in range(1, len(coins)):
    for j in range(1, len(dp)):
        if j - coins[i] >= 0:
            dp[j] = dp[j] + dp[j - coins[i]]

print(dp[int(k)])
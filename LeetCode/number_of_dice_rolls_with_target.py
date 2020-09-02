class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # optimized solution
        # Using DP Knapsack
        dp = [[0 for _ in range(dd * f + 1)] for dd in range(d + 1)]

        if target == 0 or target > d * f:
            return 0

        for i in range(1, f + 1):
            dp[1][i] = 1

        MOD = 10 ** 9 + 7
        for i in range(2, d + 1):
            for j in range(1, target + 1):
                for k in range(1, f + 1):
                    if 0 <= j - k < len(dp[i - 1]):
                        dp[i][j] += dp[i - 1][j - k]

        return dp[d][target] % MOD

    def numRollsToTarget2(self, d:int, f:int, target: int) ->int:

        dp = [[0 for _ in range(dd * f + 1)] for dd in range(d + 1)]

        if target == 0 or target > d * f:
            return 0

        for i in range(1, f + 1):
            dp[1][i] = 1

        MOD = 10 ** 9 + 7
        for i in range(2, d + 1):
            for j in range(i, d * f + 1):
                for k in range(1, f + 1):
                    if 0 <= j - k < len(dp[i - 1]):
                        dp[i][j] += dp[i - 1][j - k]

        return dp[d][target] % MOD

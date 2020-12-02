from typing import List

# Knapsack Problem
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)
        if s % 2 == 1:
            return False
        subsetSum = s // 2
        dp = [[False for _ in range(subsetSum + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subsetSum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        # print(dp)
        return dp[-1][-1]

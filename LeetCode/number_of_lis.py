from typing import List


class Solution:
    def findNumberOfLis(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        counts = [1 for _ in range(len(nums))]

        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if dp[i] >= dp[j]:
                        dp[j] = 1 + dp[i]
                        counts[j] = counts[i]
                    elif dp[i] + 1 == dp[j]:
                        counts[j] += counts[j]

        longest = max(dp)
        return sum(c for i, c in enumerate(counts) if dp[i] == longest)
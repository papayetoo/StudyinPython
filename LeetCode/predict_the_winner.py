# Dynammic Programming 문제
# DP 정의 : i 개의 리스트에서 뽑을 수 있는 최대 점수 (Player 무관)
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [nums[0]]
        n = len(nums)
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], )

class Solution:
    def climbStairs(self, n:int):
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs([10, 15, 20]))
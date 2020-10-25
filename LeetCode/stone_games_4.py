import math


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        # dp[i] for alice win
        for i in range(1, n + 1):
            if math.sqrt(i) == math.floor(math.sqrt(i)):
                dp[i] = True
                continue
            j = math.isqrt(i)
            while j >= 1:
                dp[i] |= not dp[i - j ** 2]
                if dp[i]:
                    break
                j -= 1
        return dp[-1]


if __name__ == '__main__':
    n = 10
    print(Solution().winnerSquareGame(n))

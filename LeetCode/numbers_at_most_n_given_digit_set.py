from typing import List
from collections import defaultdict
import math


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        S = str(n)
        K = len(S)
        dp = [0] * K + [1]

        for i in range(K-1, -1, -1):
            for digit in digits:
                if digit < S[i]:
                    dp[i] += len(digits) ** (K-i-1)
                elif digit == S[i]:
                    dp[i] += dp[i+1]

        return dp[0] + sum(len(digits) ** i for i in range(1, K))


if __name__ == '__main__':
    sol = Solution()
    digits = ["1","4","9"]
    n = 1000000000
    print(sol.atMostNGivenDigitSet(digits, n))

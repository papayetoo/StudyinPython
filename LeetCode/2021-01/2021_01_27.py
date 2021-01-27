import math


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        answer = 1
        MOD = 10 ** 9 + 7
        for i in range(2, n + 1):
            size = int(math.log2(i)) + 1
            answer = (answer << size) + i
            answer %= MOD
        return answer
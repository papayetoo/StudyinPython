class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K == 1:
            return 1
        if K % 2 == 0 or K % 5 == 0:
            return -1

        i = 0
        s = 1
        while True:
            if s % K == 0:
                return i + 1
            s = s * 10 + 1
            s %= K
            i += 1
        return -1
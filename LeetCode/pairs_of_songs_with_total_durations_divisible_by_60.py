from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod = defaultdict(list)
        for index, t in enumerate(time):
            mod[t % 60].append(index)

        n = len(mod[0])
        answer = (n ** 2 - n) // 2
        for i in range(1, 30):
            answer = answer + len(mod[i]) * len(mod[60 - i])
        n = len(mod[30])
        answer += (n ** 2 - n) // 2

        return answer
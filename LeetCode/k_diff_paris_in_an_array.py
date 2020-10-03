from collections import defaultdict
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1

        answer = set()
        for num in dic:
            if k > 0:
                if num - k in dic:
                    answer.add((num - k, num))
                elif num + k in dic:
                    answer.add((num, num + k))
            else:
                if dic[num] >= 2:
                    answer.add((num, num))

        return len(answer)
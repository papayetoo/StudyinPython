from collections import defaultdict
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = defaultdict(int)
        n = len(nums)
        i = 0
        while i < len(nums):
            count[nums[i]] += 1
            if 0 < count[nums[i]] < 3:
                i += 1
                continue
            else:
                del nums[i]
                continue

        return sum([x for x in count.values()])

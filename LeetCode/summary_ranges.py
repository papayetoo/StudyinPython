from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        answer = []
        i = 0
        while i < n:
            start = end = i
            while end + 1 < n and nums[end + 1] == nums[end] + 1:
                end += 1
            result = f'{nums[start]}->{nums[end]}' if start < end else f'{nums[start]}'
            answer.append(result)
            i = end + 1
        if i == n - 1:
            answer.append(result)

        return answer
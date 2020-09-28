from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k <= 1:
            return 0

        j = 0
        product = 1
        answer = 0

        for i in range(n):
            product *= nums[i]
            while product >= k:
                product //= nums[j]
                j += 1
            answer += i - j + 1

        return answer
from typing import List
from random import randint


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        first = [0] * (len(nums))
        first[0] = nums[0]
        first[1] = max(first[0], nums[1])

        for i in range(2, len(nums) - 1):
            first[i] = max(first[i - 2] + nums[i], first[i - 1])

        second = [0] * (len(nums))
        second[0] = nums[1]
        second[1] = max(second[0], nums[2])
        for i in range(2, len(nums) - 1):
            second[i] = max(second[i - 2] + nums[i + 1], second[i - 1])

        return max(max(first), max(second))

    def rob2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        n = len(nums)
        includeFirst = [0 for _ in range(n)]
        includeFirst[0] = nums[0]
        for i in range(1, n - 1):
            if i == 1:
                includeFirst[i] = max(nums[i], includeFirst[i - 1])
                continue
            includeFirst[i] = max(nums[i] + includeFirst[i - 2], includeFirst[i - 1])
        excludeFirst = [0 for _ in range(n)]
        excludeFirst[1] = nums[1]
        for i in range(2, n):
            if i == 2:
                excludeFirst[i] = max(nums[i], excludeFirst[i - 1])
                continue
            excludeFirst[i] = max(nums[i] + excludeFirst[i - 2], excludeFirst[i - 1])
        print(includeFirst)
        print(excludeFirst)
        return max(includeFirst[-2], excludeFirst[-1])


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    # nums = [2, 3, 2]
    # nums = [randint(1, 100) for _ in range(100)]
    nums = [1, 3, 1, 3, 100]
    sol = Solution()
    print(sol.rob(nums))
    print(sol.rob2(nums))

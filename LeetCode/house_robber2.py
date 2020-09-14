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
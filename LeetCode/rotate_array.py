from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nk = k % n

        if nk == 0:
            return

        nums.reverse()
        st = 0
        end = nk - 1
        while st < end:
            nums[st], nums[end] = nums[end], nums[st]
            st += 1
            end -= 1
        st = nk
        end = n - 1
        while st < end:
            nums[st], nums[end] = nums[end], nums[st]
            st += 1
            end -= 1


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    # nums = [-1,-100,3,99]
    # k = 2
    Solution().rotate(nums, k)
    print(nums)

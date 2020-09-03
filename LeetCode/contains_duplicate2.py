from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        if len(nums) <= 1 or k == 0 or t < 0:
            return False

        if t == 0 and len(set(nums)) == len(nums):
            return False

        length = len(nums)
        for i in range(length):
            for j in range(1, k + 1):
                if i + j >= length:
                    break
                else:
                    if abs(nums[i] - nums[i + j]) <= t:
                        return True
        return False


if __name__ == '__main__':
    s = Solution()
    arr= [i+1 for i in range(100)]
    arr.reverse()
    k = 100
    t = 1
    print(s.containsNearbyAlmostDuplicate(arr, k, t))
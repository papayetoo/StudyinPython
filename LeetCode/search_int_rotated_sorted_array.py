from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if target not in nums:
            return -1

        pivot = -1
        n = len(nums)
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                continue
            else:
                pivot = i + 1
                break

        def binarySearch(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                    continue
                elif nums[mid] > target:
                    right = mid - 1
                    continue
                elif nums[mid] == target:
                    return mid
            return -1

        l = binarySearch(0, pivot-1)
        r = binarySearch(pivot, n-1)
        if l == -1 and r == -1:
            return -1
        elif l != -1 and r == -1:
            return l
        elif l == -1 and r != -1:
            return r


if __name__ == "__main__":
    sol = Solution()
    # nums = [4,5,6,7,0,1,2]
    # k = 0
    nums = [3, 1]
    k = 3
    print(sol.search(nums, k))
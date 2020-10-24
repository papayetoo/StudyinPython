from typing import List
from random import randint

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s3 = -float('inf')
        stack = []
        for num in nums[::-1]:
            if num < s3:
                return True
            while stack and stack[-1] < num:
                s3 = stack.pop()
            stack.append(num)
        return False

if __name__ == '__main__':
    # nums = [1,2,3,4]
    # nums = [3,1,4,2]
    # nums = [randint(-10**9, 10**9) for _ in range(10**4)]
    nums = [2,5,0,3,4]
    print(nums)
    sol = Solution()
    print(sol.find132pattern(nums))
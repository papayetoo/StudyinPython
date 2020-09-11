from typing import List
class Solution:
    def maxProduct(self, nums:List[int]) -> int:
        maxProduct = [nums[0]]
        minProduct = [nums[0]]

        for i in range(1, len(nums)):
            maxProduct.append(max(maxProduct[i-1] * nums[i], minProduct[i-1] * nums[i], nums[i]))
            minProduct.append(min(maxProduct[i-1] * nums[i], minProduct[i-1] * nums[i], nums[i]))

        return max(maxProduct)


from typing import List
class Solution:
    def buySellStock(self, prices: List[int]) -> int:
        # Kadane Algorithm
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            if minPrice > price:
                minPrice = price
            else:
                maxProfit = max(maxProfit, price - minPrice)
        return maxProfit
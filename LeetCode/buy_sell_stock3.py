from itertools import combinations
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        transaction = []
        max_profit = 0
        min_price = prices[0]
        count = 0
        for i in range(1, len(prices)):
            print(transaction)
            if min_price > prices[i]:
                transaction.append(max_profit)
                min_price = prices[i]
                count += 1
            else:
                print(f'else min_price {min_price}')
                if max_profit < prices[i] - min_price:
                    max_profit = prices[i] - min_price
        print(transaction)

    def maxProfit2(self, prices: [int]) -> int:
        queue = []
        comb = list(combinations(range(len(prices)), 2))
        comb = [(i, j) for (i, j) in comb if prices[i] < prices[j] and i < j]
        print(comb)
        return 0

    def maxProfit3(self, prices:[int]) -> int:

        # forward max profit finding
        min_price = float('inf')
        first_profit = [0] * len(prices)
        total_profit = 0
        for i in range( len(prices)):
            min_price = min(min_price, prices[i])
            total_profit = max(total_profit, prices[i] - min_price)
            first_profit[i] = total_profit

        max_price = float('-inf')
        for j in range(len(prices)-1, 0, -1):
            max_price = max(max_price, prices[j])
            profit = max_price - prices[j]
            total_profit = max(total_profit, first_profit[j-1] + profit)

        return total_profit


if __name__ == '__main__':
    s = Solution()
    # arr =[3,3,5,0,0,3,1,4]
    # arr =[i + 1 for i in range(0, 5)]
    arr =[8,3,6,2,8,8,8,4,2,0,7,2,9,4,9]
    # arr = [1,2,4,2,5,7,2,4,9,0]
    print(s.maxProfit2(arr))
class Solution:
    def bestBuySellStock(self, prices:[int], K: int):
        temp = [0]
        profit = {}
        for t in temp:
            min_price = float('inf')
            tmp_profit = []
            min_index = t
            cur_profit = 0
            for index in range(t, len(prices)):
                if prices[index] <= min_price:
                    min_price = prices[index]
                    min_index = index
                cur_profit = max(cur_profit, prices[index] - min_price)
                tmp_profit.append(cur_profit)
            if min_index not in temp:
                temp.append(min_index)
            profit[t] = tmp_profit
        max_profit = 0
        n = 0
        sell_day = 0
        for day in profit:
            if day >= sell_day:
                sell_day = profit[day].index(max(profit[day]))
                print(sell_day)
                max_profit += profit[day][sell_day]
            else:
                continue


    def maxProfit(self, prices: [int], K: int):
        dp = [[[0 for _ in range(len(prices))] for _ in range(len(prices))] for _ in range(K+1)]

        for i in range(len(prices)):
            min_price = float('inf')
            max_profit = 0
            for j in range(i+1, len(prices)):
                min_price = min(prices[j], min_price)
                max_profit = max(max_profit, prices[j] - min_price)
                dp[1][i][j] = max_profit

        for k in range(2, K):


        print(dp)



if __name__ == '__main__':
    # prices = [i for i in range(10000, -1, -1)]
    # prices = [i for i in range(10000)]
    prices = [3, 2, 6, 5, 0, 2, 0, 3]
    # prices = [2,4,1]
    s = Solution()
    s.maxProfit(prices, 3)
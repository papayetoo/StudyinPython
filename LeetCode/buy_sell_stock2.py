class Solution:
    def buySellStock(self, prices: [int]) -> int:
        if len(prices) == 0:
            return 0
        profit = 0

        pair_prices = [(index, value) for index, value in enumerate(prices)]
        descending = sorted(pair_prices,
                            key=lambda x: x[1],
                            reverse=True)
        ascending = sorted(pair_prices,
                           key=lambda x: x[1])

        for d in descending:
            tmp = 0
            for a in ascending:
                if d[0] >= a[0]:
                    continue
                else:
                    if tmp < a[1] - d[1]:
                        tmp = a[1] - d[1]
                        print(tmp)
            profit += tmp
        return profit


if __name__ == '__main__':
    prices = [1, 2, 3, 4, 5]
    s = Solution()
    print(s.buySellStock(prices))

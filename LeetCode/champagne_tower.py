class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[1]]
        polySum = [2 ** x for x in range(101)]
        wholeSum = [2 ** (x + 1) - 1 for x in range(101)]
        for i in range(1, 10):
            tmp = []
            for j in range(i + 1):
                if j - 1 >= 0 and j < i:
                    tmp.append(dp[-1][j - 1] + dp[-1][j])
                elif j - 1 >= 0:
                    tmp.append(dp[-1][j - 1])
                elif j < i + 1:
                    tmp.append(dp[-1][j])
            dp.append(tmp)

        liquid = poured
        while liquid > 0:
            if liquid - polySum[i]:
                liquid -= polySum[i]
            else:
                break
            i += 1
        print(i)
        return 0.
        # if query_row < i:
        #     return 1.0
        # elif query_row == i:
        #     return liquid * dp[query_row][query_glass]/polySum[i]
        # else:
        #     return 0.0


if __name__ == '__main__':
    sol = Solution()
    print(sol.champagneTower(100000009, 2, 0))

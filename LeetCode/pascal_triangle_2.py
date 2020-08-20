class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        dp = [[0 for _ in range(34)] for _ in range(34)]
        dp[0][0] = 1
        for i in range(1, 34):
            for j in range(i+1):
                if j - 1 < 0:
                    dp[i][j] = dp[i-1][j]
                    continue
                if j > i:
                    dp[i][j] = dp[i-1][j-1]
                    continue
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp[rowIndex][:rowIndex+1]

    def getRow2(self, rowIndex: int) -> [int]:
        result = [1]
        for i in range(0, rowIndex):
            for j in range(i, 0, -1):
                result[j] = result[j] + result[j-1]
            result.append(1)
        return result

    def getRow3(self, rowIndex: int)->[int]:
        result = [[1] * (i+1) for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(i+1):
                if 0 < j < i:
                    # 처음과 끝 값에 계산할 필요가 없어 빠름
                    result[i][j] = result[i-1][j] + result[i-1][j-1]
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.getRow2(3))
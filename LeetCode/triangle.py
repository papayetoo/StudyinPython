from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0][0]]

        if len(dp) == 1:
            return triangle

        for i in range(1, len(triangle)):
            new_dp = []
            for j in range(len(triangle[i])):
                if 1 <= j < len(dp):
                    new_dp.append(min(dp[j - 1] + triangle[i][j], dp[j] + triangle[i][j]))
                    continue
                elif j - 1 < 0:
                    new_dp.append(dp[j] + triangle[i][j])
                    continue
                elif j >= len(dp):
                    new_dp.append(dp[-1] + triangle[i][j])
            dp = new_dp

        return min(dp)


if __name__ == '__main__':
    tri = [[2],[3,4],[6,5,9],[4,4,8,0]]
    s = Solution()
    print(s.minumumTotal2(tri))
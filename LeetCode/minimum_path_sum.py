# Minimum Path Sum
# Difficulty: Medium
# Category : DP
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                from_up = dp[r][c - 1] if c - 1 >= 0 else float('inf')
                from_left = dp[r - 1][c] if r - 1 >= 0 else float('inf')
                dp[r][c] = grid[r][c] + min(from_up, from_left)

        return dp[rows - 1][cols - 1]


if __name__ == '__main__':
    inArr = [[1,3,1],[1,5,1],[4,2,1]]
    s = Solution()
    print(s.minPathSum(inArr))
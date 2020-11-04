from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])

        healths = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if dungeon[r][c] > 0:
                    healths[r][c] = 1
                    continue
                healths[r][c] = dungeon[r][c]

        for r in range(rows):
            for c in range(cols):
                healths[r][c] = max(healths[r-1][c] if r - 1 >= 0 else 0, healths[r][c-1] if c - 1 >= 0 else 0) + healths[r][c]

        for line in healths:
            print(line)
        return abs(healths[-1][-1]) + 1 if healths[-1][-1] <= 0 else healths[-1][-1]



if __name__ == '__main__':
    sol = Solution()
    # dungeon = [[0,5],[-2,-3]]
    dungeon = [[-2,-3, 3],[-5,-10, 1], [10, 30, -5]]
    sol.calculateMinimumHP(dungeon)

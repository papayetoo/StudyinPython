from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])

        healths = [[0] * cols for _ in range(rows)]
        healths[0][0] = dungeon[0][0]

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                # Plus 되는 체력을 배제
                if r == 0:
                    result = healths[r][c - 1] + dungeon[r][c]
                    healths[r][c] = healths[r][c - 1] + dungeon[r][c] if result <= 0 else healths[r][c - 1]
                    # if dungeon[r][c] <= 0:
                    #     healths[r][c] = healths[r][c-1] + dungeon[r][c]
                    # else:
                    #     healths[r][c] = healths[r][c-1]
                    continue
                if c == 0:
                    result = healths[r - 1][c] + dungeon[r][c]
                    healths[r][c] = healths[r - 1][c] + dungeon[r][c] if result <= 0 else healths[r-1][c]
                    # if dungeon[r][c] <= 0:
                    #     healths[r][c] = healths[r-1][c] + dungeon[r][c]
                    # else:
                    #     healths[r][c] = healths[r-1][c]
                    continue
                else:
                    left = healths[r][c-1] + dungeon[r][c]
                    up = healths[r-1][c] + dungeon[r][c]
                    m = max(left, up)
                    healths[r][c] = max(left, up) + dungeon[r][c] if max(left, up) <= 0 else max(left,up)
                    # if dungeon[r][c] <= 0:
                    #     healths[r][c] = max(left, up) + dungeon[r][c]
                    # else:
                    #     healths[r][c] = max(left, up)
                    continue

        # for c in range(cols):
        #     if healths[0][c] < 0:
        #         minHealths[0][c] = abs(healths[0][c]) + 1
        #     else:
        #         minHealths[0][c] = minHealths[0][c-1] if c - 1 >= 0 else 0
        #
        # for r in range(rows):
        #     if healths[r][0] < 0:
        #         minHealths[r][0] = abs(healths[r][0]) + 1
        #     elif healths[r][0] > 0:
        #         minHealths[r][0] = minHealths[r-1][0] if r - 1 > 0 else 1
        #     else:
        #         minHealths[r][0] = 1
        #
        # for c in range(cols):
        #     if healths[0][c] < 0:
        #         minHealths[0][c] = abs(healths[0][c]) + 1
        #     elif healths[0][c] > 0:
        #         minHealths[0][c] = minHealths[0][c-1] if c - 1 > 0 else 1
        #     else:
        #         minHealths[0][c] = 1
        #
        # for r in range(1, rows):
        #     for c in range(1, cols):
        #         minHealths[r][c] = min(minHealths[r-1][c], minHealths[r][c-1])

        for line in healths:
            print(line)


if __name__ == '__main__':
    sol = Solution()
    dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    sol.calculateMinimumHP(dungeon)

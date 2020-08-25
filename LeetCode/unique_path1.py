class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]

        # 최적화 코드
        for c in range(n):
            grid[0][c] = 1
        for r in range(1, m):
            grid[r][0] = 1

        for r in range(1,m):
            for c in range(1,n):
                # 최적화 코드
                if r == 0 or c == 0:
                    continue
                # index out of bound 문제를 벗어나기 위해
                # fromLeft, fromUp을 이용
                fromLeft = grid[r][c-1] if c - 1 >= 0 else 0
                fromUp = grid[r-1][c] if r - 1 >= 0 else 0
                grid[r][c] = fromLeft + fromUp
        return grid[-1][-1]
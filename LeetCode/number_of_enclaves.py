from typing import List


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:

        rows = len(A)
        if rows == 0:
            return 0
        cols = len(A[0])

        dy = [1, -1, 0, 0]
        dx = [0, 0, 1, -1]

        def markingLand(y, x):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < rows and 0 <= nx < cols and A[ny][nx] == 1:
                    A[ny][nx] = 2
                    markingLand(ny, nx)
            A[y][x] = 2

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and A[r][c] == 1:
                    markingLand(r, c)

        answer = [(x, y) for x in range(rows) for y in range(cols) if A[x][y] == 1]
        print(answer)
        return len(answer)

if __name__ == '__main__':
    A = [[0,0,0,0],
         [1,0,1,0],
         [0,1,1,0],
         [0,0,0,0]]
    sol = Solution()
    sol.numEnclaves(A)
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = []
        dy = [1, -1, 0, 0]
        dx = [0, 0, 1, -1]

        def dfs(y, x):
            if y < 0 or y >= rows or x < 0 or x >= cols:
                return
            visited.append((y, x))
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < rows and 0 <= nx < cols and board[ny][nx] == 'O' and (ny, nx) not in visited:
                    board[ny][nx] = 'T'
                    dfs(ny, nx)
            board[y][x] = 'T'

        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and board[i][j] == 'O':
                    dfs(i, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        for r in range(rows):
            print(board[r])


if __name__ == '__main__':
    # board = [['X', 'X', 'X', 'X'],
    #          ['X', 'O', 'O', 'O'],
    #          ['X', 'X', 'O', 'X'],
    #          ['X', 'O', 'X', 'X']]
    # board = [['X', 'X', 'X'],
    #          ['X', 'O', 'X'],
    #          ['X', 'X', 'X']]
    board = [['O', 'O', 'O'],
             ['O', 'O', 'O'],
             ['O', 'O', 'O']]
    # board =[["X", "X", "X", "O", "X", "O", "X"],
    #         ["X", "O", "X", "O", "X", "O", "O"],
    #         ["X", "X", "X", "X", "X", "X", "O"],
    #         ["X", "X", "X", "X", "O", "X", "O"],
    #         ["X", "X", "X", "X", "X", "X", "O"],
    #         ["X", "X", "X", "X", "X", "X", "X"],
    #         ["O", "X", "X", "O", "O", "O", "X"]]
    # board = [["O", "X", "O", "O", "O", "O", "O", "O", "O"],
    #          ["O", "O", "O", "X", "O", "O", "O", "O", "X"],
    #          ["O", "X", "O", "X", "O", "O", "O", "O", "X"],
    #          ["O", "O", "O", "O", "X", "O", "O", "O", "O"],
    #          ["X", "O", "O", "O", "O", "O", "O", "O", "X"],
    #          ["X", "X", "O", "O", "X", "O", "X", "O", "X"],
    #          ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
    #          ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
    #          ["O", "O", "O", "O", "O", "X", "X", "O", "O"]]
    '''
    [["O","X","O","O","O","O","O","O","O"],
    ["O","O","O","X","O","O","O","O","X"],
    ["O","X","O","X","O","O","O","O","X"],
    ["O","O","O","O","X","O","O","O","O"],
    ["X","O","O","O","O","O","O","O","X"],
    ["X","X","O","O","X","O","X","O","X"],
    ["O","O","O","X","O","O","O","O","O"],
    ["O","O","O","X","O","O","O","O","O"],
    ["O","O","O","O","O","X","X","O","O"]]
    '''

    Solution().solve(board)

from typing import List
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        startPos = []
        obstacles = []
        endPos = []
        empty = 0
        answer = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    startPos.append(r)
                    startPos.append(c)
                elif grid[r][c] == 2:
                    endPos.append([r, c])
                elif grid[r][c] == -1:
                    obstacles.append([r, c])
                else:
                    empty += 1

        def dfs(current: [int], visited: [], emptyCount: int):
            dy = [1, -1, 0, 0]
            dx = [0, 0, 1, -1]
            nonlocal answer
            if emptyCount == 0:
                for k in range(4):
                    endY = current[0] + dy[k]
                    endX = current[1] + dx[k]
                    print(visited)
                    if 0 <= endY < rows and 0 <= endX < cols and grid[endY][endX] == 2:
                        visited.append([endY, endX])
                        answer += 1
                        visited.pop()
                return

            for i in range(4):
                ny = current[0] + dy[i]
                nx = current[1] + dx[i]
                if [ny, nx] not in visited and 0 <= ny < rows and 0 <= nx < cols and emptyCount > 0 and grid[ny][
                    nx] == 0:
                    visited.append([ny, nx])
                    dfs([ny, nx], visited, emptyCount - 1)
                    visited.pop()

        dfs(startPos, [], empty)
        return answer


if __name__ == '__main__':
    # grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    # grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    # grid = [[0,1],[2,0]]
    grid = [[0,0,0,0,0,0,2,0,0,0],[0,0,0,0,0,0,0,0,1,0]]
    s = Solution()
    print(s.uniquePathsIII(grid))
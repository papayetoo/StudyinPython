import sys

count = 0


def dfs(grid: list, height: int, width: int, x: int, y: int, endx: int, endy: int, force: int, visited: list):
    global count
    if x == endx and y == endy:
        count += 1
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx <= height and 1 <= ny <= width and grid[ny][nx] - grid[x][y] <= force and (nx, ny) not in visited:
            visited.append((nx, ny))
            dfs(grid, height, width, nx, ny, endx, endy, force - (grid[ny][nx] - grid[x][y]), visited)
            visited.pop()


if __name__ == '__main__':
    tc = int(sys.stdin.readline().strip())
    for _ in range(tc):
        h, w, obs, force, stx, sty, ex, ey = map(int, sys.stdin.readline().split())
        grid = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
        for _ in range(obs):
            x, y, height = map(int, sys.stdin.readline().split())
            grid[x][y] = height
        dfs(grid, h, w, stx, sty, ex, ey, force, [(stx, sty)])
        if count == 0:
            print('인성 문제있어??')
        else:
            print('잘했어!!')
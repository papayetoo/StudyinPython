# 로봇 청소기
import sys

input = sys.stdin

if __name__ == "__main__":
    rows, cols = map(int, input.readline().split())
    y, x, d = map(int, input.readline().split())
    grid = [list(map(int, input.readline().split())) for _ in range(rows)]
    directions = [0, 1, 2, 3]
    forwardMove = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    backwardMove = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    isMove = True
    answer = 0
    while isMove:
        if grid[y][x] == 0:
            grid[y][x] = 2
            answer += 1
        nextDir = forwardMove[d]
        if grid[y + nextDir[0]][x + nextDir[1]] == 0:
            y += nextDir[0]
            x += nextDir[1]
            if d == 0:
                d = 3
            elif d == 1:
                d = 0
            elif d == 2:
                d = 1
            elif d == 3:
                d = 2
            continue
        else:
            count = 0
            for i in range(4):
                adjY = y + forwardMove[i][0]
                adjX = x + forwardMove[i][1]
                if 0 <= adjY < rows and 0 <= adjX < cols and grid[adjY][adjX] == 1 or grid[adjY][adjX] == 2:
                    count += 1
            backY = backwardMove[d][0] + y
            backX = backwardMove[d][1] + x
            if count == 4 and grid[backY][backX] == 1:
                isMove = False
                break
            elif count == 4 and grid[backY][backX] != 1:
                y = backY
                x = backX
                continue
            elif count != 4 and grid[nextDir[0]][nextDir[1]] == 1:
                if d == 0:
                    d = 3
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 2
                continue
    print(answer)
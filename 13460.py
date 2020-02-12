import sys, collections
row, col = map(int, input().split())
maps = [[" " for _ in range(col)] for _ in range(row)]
redRow = -1
redCol = -1
blueRow = -1
blueCol = -1
for i in range(row):
    tempRow = input()
    for j in range(col):
        maps[i][j] = tempRow[j]
        if tempRow[j] == 'R':
            redRow = i
            redCol = j
        elif tempRow[j] == 'B':
            blueRow = i
            blueCol = j

def moveRed(startRow, startCol):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    px = 2
    py = 2
    queue = []
    pair = (startRow, startCol)
    queue.append(pair)
    directionCount = 0
    dirQueue = []

    while len(queue) != 0:
        temp = queue.pop()
        maps[temp[0]][temp[1]] = 'C'
        for i in range(4):
            if(temp[0] + dy[i] >=0 and temp[0] + dy[i] < row and temp[1] + dx[i] >= 0 and temp[1] + dx[i] < col) :
                if(maps[temp[0] + dy[i]][temp[1]+dx[i]] == 'O'):
                    dirQueue.append((dy[i], dx[i]))
                    if py != dy[i] and px != dx[i]:
                        directionCount += 1
                        py = dy[i]
                        px = dx[i]
                    return directionCount, dirQueue
        for i in range(4):
            if (maps[temp[0] + dy[i]][temp[1] + dx[i]] == '.'):
                maps[temp[0] + dy[i]][temp[1] + dx[i]] = 'R'
                pair = (temp[0] + dy[i], temp[1] + dx[i])
                dirQueue.append((dy[i], dx[i]))
                if py != dy[i] and px != dx[i]:
                    directionCount += 1
                    py = dy[i]
                    px = dx[i]
                queue.append(pair)

def moveBlue(blueRow, blueCol, redMovingArr=[()]):
    while len(redMovingArr) != 0:
        temp = redMovingArr.pop()
        if(blueRow + temp[0] >= 0 and blueRow + temp[0] < row and blueCol + temp[1] >= 0 and blueCol + temp[1] < col and maps[blueRow + temp[0]][blueCol + temp[1]] != '#'):
            maps[blueRow][blueCol] = 'C'
            blueRow += temp[0]
            blueCol += temp[1]
            maps[blueRow][blueCol] = 'B'

answer, movingArr = moveRed(redRow, redCol)
while len(movingArr) != 0:
    temp = movingArr.pop()
    if (blueRow + temp[0] >= 0 and blueRow + temp[0] < row and blueCol + temp[1] >= 0 and blueCol + temp[1] < col and
            maps[blueRow + temp[0]][blueCol + temp[1]] != '#'):
        maps[blueRow][blueCol] = 'C'
        blueRow += temp[0]
        blueCol += temp[1]
        maps[blueRow][blueCol] = 'B'

dx = [0,0,1,-1]
dy = [1,-1,0,0]
count = 0
for i in range(4):
    if(blueRow + dy[i] >= 0 and blueRow + dy[i] < row and blueCol + dx[i] >= 0  and blueCol + dx[i] < col and maps[blueRow + dy[i]][blueRow + dx[i]] == 'O'):
        count += 1

if count != 0 or answer > 10:
    print(-1)
else:
    print(answer)

for i in range(row):
    print(maps[i])
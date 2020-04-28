import sys

def initpos(arr:[], size:int):
    fishpos = []
    sharkpos = ()
    for i in range(size):
        for j in range(size):
            if arr[i][j] == 9:
                sharkpos = (i, j)
            elif 1<= arr[i][j] <=6 :
                fishpos.append((i, j, arr[i][j]))

    return fishpos, sharkpos

def callmom(arr:[], fishpos:[], babysize:int):

    cnt = 0

    if fishpos == 0:
        return True

    for infos in fishpos:
        if infos[2] < babysize:
            cnt += 1


    if cnt == 0: # 끝내도 됨
        return True
    else:
        return False

def move(grid:[], fishpos:[], sharkpos:[], babysize:int, time:int):
    # 큰 물고기가 있는 칸은 지나갈 수 없다는 것 위반

    global eatcount

    if len(fishpos) == 0:
        return time

    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    copy = grid.copy()
    while not callmom(grid, fishpos, babysize):
        for i in range(4):
            if N > sharkpos[0] + dy[i] >=0 and N > sharkpos[1] + dx[i] >=0 and babysize > copy[sharkpos[0] + dy[i]][sharkpos[1] + dx[i]] :
                move(copy, fishpos, sh)


# 입력 받는 부분
N = int(input())
grid = []
for i in range(N):
    grid.append( list(map(int, sys.stdin.readline().split()))  )
babysize = 2
eatcount = 0
fishpos, sharkpos = initpos(grid, N)
time = 0
for i in range(N):
    print(grid[i])
print('====== babysize {} Time {}======'.format( babysize, time) )

# 값을 가공하는 부분.
time, babysize, sharkpos = move(grid, fishpos, sharkpos, babysize, time)
for i in range(N):
    print(grid[i])
print('====== babysize {} Time {}======'.format( babysize, time) )
while not callmom(grid, fishpos, babysize):
    time,babysize, sharkpos = move(grid, fishpos, sharkpos, babysize, time)
    for i in range(N):
        print(grid[i])
    print('====== babysize {} Time {}======'.format( babysize, time) )
print(time)
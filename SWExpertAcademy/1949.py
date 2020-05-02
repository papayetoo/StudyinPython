import copy
def solve(k: int, x: int, y: int, arr: list, visited: list, count: int):

    dy = [1,-1,0,0]
    dx = [0,0,1,-1]

    length = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < len(arr) and 0 <= ny < len(arr) and visited[ny][nx] == 0:
            if arr[y][x] > arr[ny][nx]:
                print(f'{ny},{nx} : {arr[ny][nx]}')
                visited[ny][nx] = 1
                length = max(length,  1 +solve(k, nx, ny, arr, visited, count))
                visited[ny][nx] = 1
            elif arr[y][x] > arr[ny][nx] - k and count == 1:
                arr[ny][nx] = arr[y][x] - 1 if arr[y][x] >= arr[ny][nx] else arr[ny][nx] - k
                print(f'{ny},{nx} : {arr[ny][nx]}')
                visited[ny][nx] = 1
                count -= 1
                length = max(length,  1 +solve(k, nx, ny, arr, visited, count))
                count += 1
                visited[ny][nx] = 1

    
    return length

T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    count = 1
    arr = [[0] * N] * N
    pos = []
    maxheight=0
    for r in range(N):
        arr[r] = list(map(int, input().split()))
        maxheight=max(maxheight, max(arr[r]))

    
    for r in range(N):
        for c in range(N):
            if arr[r][c] == maxheight:
                pos.append((r,c))
    
    answer = 0
    for p in pos:
        visited = [ [0 for _ in range(N)] for _ in range(N)] 
        y, x = p[1], p[0]
        visited[y][x] = 1
        print(f'{y} {x}:{arr[y][x]}')
        temp = copy.deepcopy(arr)
        answer = max(answer, solve(K, x, y, temp, visited, count))
    
    print(f'#{i} {answer}')



# custom combination
def combination(arr = [], visited =[] ,index = 0, r = 0):
    if r == 0:
        for i in range(len(arr)):
            if visited[i] == 1:
                print(arr[i], end=' ')
        print()
        return

    for i in range(index,len(arr)):
        visited[i] = 1
        combination(arr, visited, i + 1, r - 1)
        visited[i] = 0

numList = [i + 1 for i in range(10)]
visited = [0 for _ in range(10)]
combination(numList, visited, 0, 3)
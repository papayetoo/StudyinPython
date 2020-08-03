# custom combination
import sys
sys.setrecursionlimit(10**6)
def combination(arr = [], visited =[] ,index = 0, r = 0):

    if index > len(arr):
        return

    if r == 0:
        # for i in range(len(arr)):
        #     if visited[i] == 1:
        #         print(arr[i], end=' ')
        for v in visited:
            print(arr[v], end=' ')
        print()
        return

    # for 문을 이용하는 방식
    # for i in range(index,len(arr)):
    #     visited[i] = 1
    #     combination(arr, visited, i + 1, r - 1)
    #     visited[i] = 0

    # for문을 이용하지 않는 방식
    visited.append(index)
    combination(arr, visited, index + 1, r -1)
    visited.pop()
    combination(arr, visited, index + 1, r)


numList = [i for i in range(3)]
# visited = [0 for _ in range(10)]
visited = []
import time
start = time.mktime( time.localtime() )
combination(numList, visited, 0, 2)
print('time diffrence : {}'.format(start  - time.mktime( time.localtime() ) ) )


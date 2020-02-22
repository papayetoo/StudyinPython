# 백준 14891번 문제 톱니바퀴
# 시뮬레이션
import sys
def rotate(dir:int, s:str)->str:
    ret = ''
    if dir == 0:
        return s
    if dir == -1:
        ret += s[1:] + s[:1]
    elif dir == 1:
        ret += s[-1:] + s[:-1]
    return ret
def canRotate(target:int, dir:int,lst:[str]) -> dict:
    result = {i : 0 for i in range(4)}
    result[target] = dir
    cur = target
    left = target - 1
    right = target + 1

    while left >= 0:
        if result[cur] == 0:
            result[left] = 0
        elif result[cur] != 0 and lst[left][2] != lst[cur][6]:
            result[left] = -result[cur]
        else:
            result[left] = 0
        left -= 1
        cur -= 1

    cur = target
    while right < len(lst) :
        if result[cur] == 0:
            result[right] = 0
        elif result[cur] != 0 and lst[cur][2] != lst[right][6]:
            result[right] = -result[cur]
        else:
            result[right] = 0
        right += 1
        cur += 1

    return result


arr = []
for _ in range(4):
    arr.append(input())
rotNum = int(input())
rmap = []
for _ in range(rotNum):
    rmap.append(list(map(int, input().split())))
# print(rotate(-1, arr[0]))
for target, dir in rmap:
    rr = canRotate(target - 1, dir, arr)
    # print(rr)
    for i in range(4):
        arr[i] = rotate(rr[i], arr[i])
    # print(arr)

sum = 0
print(arr)
for i in range(4):
    if arr[i][0] == '1':
        sum += 2**i
print(sum)




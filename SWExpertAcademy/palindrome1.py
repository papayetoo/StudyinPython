
def solve(arr):
    answer = 0
    for r in range(8):
        for c in range(8-length+1):
            l = arr[r][c:c+length]
            if l == list(reversed(l)):
                answer += 1    
    
    return answer


T = int(input())

for i in range(1, T+1):
    answer=0
    length = int(input())
    arr = [['a'] * 8] * 8
    for r in range(8):
        arr[r] = list(input())
    answer += solve(arr)
    arr = list(map(list, zip(*arr)))
    answer += solve(arr)
    print('#{} {}'.format(i, answer))



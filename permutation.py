# 모든 순열 만들기
def permutation(numbers=[], r = 0, depth = 0):
    if depth == r:
        for i in range(0, r):
            print(numbers[i], end=' ')
        print()
        return

    for i in range(depth, len(numbers)):
        numbers[i], numbers[depth] = numbers[depth], numbers[i]
        permutation(numbers, r, depth + 1)
        numbers[i], numbers[depth] = numbers[depth], numbers[i]
# 다음 순열
def next_permutation(numbers = [])->bool:
    n = len(numbers) - 1
    i = n
    # 마지막 순열인지 검사하는 부분
    while i > 0 and numbers[i - 1] >= numbers[i]: # 내림차순인지 확인 및 마지막 순열인지 확인.
        i -= 1
    if i == 0:
        return False
    # 마지막 순열인지 검사하는 부분 종료.
    j = n
    while numbers[i - 1] >= numbers[j]:
        # [1,4,3,2]에서 numbers[i-1] = 1 numbers[j] = 2
        # j 는 감소하지 않음.
        j -= 1
    numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1] # 2, 4, 3, 1 로 변경됨.
    while i < j : # i = 1, j = 3 이므로 while 루프 돌지 않음.
        numbers[i], numbers[j] = numbers[j], numbers[i] # 2, 1, 3, 4 로 변
        i += 1
        j -= 1
    return  True
#다음 순열 업그레이드 1 [3,2,1] 다음 순열을 반환하는 순열
def next_permutation2(numbers=[]) -> None:
    n = len(numbers) - 1
    i = n
    if n == 0:
        return
    while i - 1 >= 0 and numbers[i-1] >= numbers[i]:
        i -= 1
    if i == 0: # next_permutation1 과 다른 부분.
        numbers.reverse()
        return
    j = n
    while j >= 0 and numbers[i-1] >= numbers[j]:
        j -= 1
    numbers[i-1], numbers[j] = numbers[j], numbers[i-1]
    j = n
    while i < j:
        numbers[i], numbers[j] = numbers[j], numbers[i]
        i -= 1
        j += 1
    return


numbers = [i for i in range(9, 0, -1)]
next_permutation2(numbers)
print(numbers)
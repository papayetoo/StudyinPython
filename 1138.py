import itertools, sys
sys.setrecursionlimit(10**8)
def next_perm(list = []):
    n = len(list) - 1
    i = n
    # 예시 [1, 2, 4, 3]의 경우 i 는 2 까지 감소.
    while i > 0 and list[i - 1] >= list[i]:
        i -= 1
        # 리스트 상에서 역순인 곳까지 i 감소
    if i == 0: # [1,2,3,4] 의 리스트가 주어진 경우에  [4,3,2,1] 이 마지막 순열임.
        return False
        # i 가 0 까지 감소했다면 마지막 순열임.
    j = n # j 는 리스트의 가장 마지막 원소
    while list[i - 1] >= list[j]: # [1,2,4,3]의 경우 j는 감소하지 않음.
        j -= 1
    list[i - 1], list[j] = list[j], list[i - 1] # [1,2,4,3] -> [1,3,4,2]로 변경됨.
    j = n # 변경된 리스트의 마지막 원소
    while i < j: # 현재 i = 2, j = 3
        list[i], list[j] = list[j], list[i] # [1,3,4,2] -> [1,3,2,4] 임
        i += 1
        j -= 1
    return True
def perm(shorterList = [], n = 0, r= 0,depth = 0):
    if depth == r :
        print(shorterList, sep=' ')
        return
    for i in range(depth, n):
        shorterList[i], shorterList[depth] = shorterList[depth], shorterList[i]
        perm(shorterList, n, r, depth + 1)
        shorterList[i], shorterList[depth] = shorterList[depth], shorterList[i]

def solution(n = 0, shorterList = []):
    heightList = [i + 1 for i in range(n)]
    count = 0
    while True:
        count = 0
        for i in range(len(shorterList)):
            correct = shorterList[i]
            height = i + 1
            index = heightList.index(height)
            longerCount = 0
            for k in range(0, index):
                if heightList[k] > height:
                    longerCount += 1
            if longerCount == correct:
                count += 1
            else:
                break
        if count == n:
            for value in heightList:
                print(value, end=' ')
            return
        else:
            next_perm(heightList)
            continue

n = int(input())
# 사람 수
shorter = list(map(int, input().split()))
# 자기보다 작은 사람 수
solution(n, shorter)

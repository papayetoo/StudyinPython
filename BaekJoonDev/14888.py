# 연산자 끼워넣기
import itertools
import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
samples = ['+', '-', '*', '//']
rop = []
for i, val in enumerate(op):
    if val > 0 :
        for _ in range(val):
            rop.append(samples[i])
lst = list(set(itertools.permutations(rop, N-1))) # 중복 제거
# 안하면 시간초과 발생
maxanswer, minanswer = -1e9, 1e9


for index, operators in enumerate(lst):
    result = nums[0]
    for cur in range(N-1):
        next = cur + 1
        if operators[cur] == '+':
            result = result + nums[next]
        elif operators[cur] == '-':
            result = result - nums[next]
        elif operators[cur] == '*':
            result = result * nums[next]
        elif operators[cur] == '//':
            if result >= 0 :
                result = result // nums[next]
            else:
                result = -((-result) //nums[next])
    maxanswer = int(max(maxanswer, result))
    minanswer = int(min(minanswer, result))
print(maxanswer,minanswer, sep='\n')



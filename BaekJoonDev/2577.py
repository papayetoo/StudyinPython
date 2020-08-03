# 구현 알고리즘
from itertools import groupby
a = int(input())
b = int(input())
c = int(input())
answer = str(a * b * c)
sol = [0] * 10
for i in answer:
    sol[int(i)] += 1
for x in sol:
    print(x)


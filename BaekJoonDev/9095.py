# 1,2,3 더하기
numbers = [0, 1, 2, 4]
for i in range(4, 11):
    numbers.append(numbers[i-1]+numbers[i - 2]+numbers[i-3])

i=int(input())
answer = []
for j in range(i):
    answer.append(int(input()))

for x in answer:
    print(numbers[x])
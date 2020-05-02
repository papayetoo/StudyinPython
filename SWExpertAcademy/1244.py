# 최대 상금
def permutation(depth):

    if depth == len(lst):
        temp = []
        for i in range(len(lst)):
            temp.append(lst[i])
        num = ''.join(temp)
        result.append(num)

    for i in range(depth, len(lst)):
        lst[i], lst[depth] = lst[depth], lst[i]
        permutation(depth+1)
        lst[i], lst[depth] = lst[depth], lst[i]

T = int(input())
answers = []
for k in range(T):
    result = []
    numinfo, changenum = input().split()
    changenum = int(changenum)
    tans = 0
    cnt = 0
    for j in range(len(numinfo)-1):
        lst = list(map(int, [*numinfo]))
        while cnt < changenum:
            for i in range(j+1, len(lst)):
                lst[j], lst[i] = lst[i], lst[j]
                print(lst)
            cnt +=1


for index, value in enumerate(answers):
    print('#{} {}'.format(index+1, value))

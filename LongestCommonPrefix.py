def longetCommonPrefix(strs =[str], compare='')->str:
    for i in range(len(compare), -1, -1):
        s = compare[0:i]
        j = 1
        flag = True
        while j < len(strs):
            if strs[j].find(s) == -1:

                flag = False
                break
            else:
                print(strs[j].find(s))
                j += 1

        if flag is True:
            return s

    return ''
strs = list(input().split())
answer = longetCommonPrefix(strs, strs[0])
print(answer)
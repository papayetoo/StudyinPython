str = input()

def addSharpChar(string):
    result = "#"
    length = len(string)
    for i in range(0,length):
        result += string[i]
        result += "#"
    result += "#"
    return  result

def manacher(sharpedString):
    a = [0] * len(sharpedString)
    p = 0  ## 중심점 p = 0 초기화
    r = 0  ## 시작점에서 가장 먼 반경 초기화.
    for i in range(0, len(sharpedString)) :
        if(i <= r) :
            a[i] = min(r - i, a[2*p - i])
        else:
            a[i] = 0

        while i - a[i] - 1 >= 0 and i + a[i] + 1 < len(sharpedString) and sharpedString[i - a[i] -1] == sharpedString[i + a[i] + 1]:
            a[i] += 1

        if( r < i + a[i]) :
            r = i + a[i]
            p = i
    return a
manacherResult = manacher(addSharpChar(str))
print(max(manacherResult))


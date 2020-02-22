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

    maxIndex = a.index(max(a))
    for i in range(maxIndex - a[maxIndex], maxIndex + a[maxIndex] + 1):
        if sharpedString[i] != '#':
            print(sharpedString[i],end='')
    return a
class Solution:
    def countSubstrings(self, s: str) -> int:
        manacher = '#'
        for c in s:
            manacher += c
            manacher += '#'

        arr = [0 for _ in range(len(manacher))]
        r = 0
        p = 0

        for i in range(len(manacher)):
            if i <= r:
                arr[i] = min(r - i, arr[2 * p - i])
            else:
                arr[i] = 0

            while arr[i] + 1 <= i < len(manacher) - arr[i] - 1 and manacher[i - arr[i] - 1] == manacher[i + arr[i] + 1]:
                arr[i] += 1

            if i + arr[i] > r:
                p, r = i, i + arr[i]

        answer = 0
        for value in arr:
            answer += int((value + 1)/2)
        return  answer
arr = [2,2,2,2,5,5,5,8]
print(sum(arr[0:2]))
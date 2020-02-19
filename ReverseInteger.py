class Solution:
    def reverse(x: int) -> int:
        s = str(abs(x))
        arr = []
        for i in range(len(s) - 1, -1, -1):
            arr.append(s[i])
        answerStr = ''
        for i in range(len(arr)):
            answerStr += str(arr[i])
        if x < 0:
            return -int(answerStr)
        else:
            return int(answerStr)

a = int(-123)
print(Solution.reverse(a))

import math
class Solution:
    def sequentialDigits(self, low: int, high: int) -> [int]:
        answer = []
        def makeDigits(curNum: int):
            if high < curNum:
                return
            else:
                if low <= curNum <= high:
                    answer.append(curNum)
                lastDigits = curNum % 10
                if lastDigits < 9:
                    makeDigits(curNum * 10 + lastDigits + 1)

        for i in range(1, 10):
            makeDigits(i)
        answer.sort()
        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.sequentialDigits(1000, 13000))
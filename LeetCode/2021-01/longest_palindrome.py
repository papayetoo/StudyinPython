# 가장 긴 팔린드롬 문제
# Manacher 알고리즘
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def addSharp(string) -> str:
            result = '#'
            for ss in string:
                result += ss + '#'
            return result

        def manacher(string) -> str:
            sharped = addSharp(s)
            a = [0] * len(sharped)
            p = r = 0
            for i in range(len(sharped)):
                if i <= r:
                    a[i] = min(r - i, a[2 * p - i])
                else:
                    a[i] = 0

                while i - a[i] - 1 >= 0 and i + a[i] + 1 < len(sharped) and sharped[i - a[i] - 1] == sharped[
                    i + a[i] + 1]:
                    a[i] += 1

                if r < i + a[i]:
                    r = i + a[i]
                    p = i
            maxIndex = a.index(max(a))
            answer = sharped[maxIndex - a[maxIndex]:maxIndex + a[maxIndex] + 1].replace('#', '')
            return answer

        return manacher(s)



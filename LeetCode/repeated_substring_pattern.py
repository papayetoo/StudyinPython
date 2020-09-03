class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        halfLength = len(s) // 2 + 1

        for i in range(halfLength, 0, -1):
            subStr = s[:i]
            if subStr * (len(s) // len(subStr)) == s:
                return True

        return False

    def repeatedSubstringPattern2(self, s: str) -> bool:
        ss = (s + s)[1:-1]
        return ss.find(s) != -1


if __name__ == '__main__':
    s = Solution()
    s.repeatedSubstringPattern2('aba')
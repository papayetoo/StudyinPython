class Solution:
    def titleToNumber(self, s: str) -> int:
        str_size = len(s)
        answer = 0
        for index, char in enumerate(s):
            cur = index + 1
            answer += (26 ** (str_size - cur)) * (ord(char) - ord('A') + 1)
        return answer
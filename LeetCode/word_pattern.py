class Solution:
    def wordPattern(self, pattern: str, s: str):
        dic = {}
        words = s. split()

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):

            if ord(pattern[i]) not in dic:
                dic[ord(pattern[i])] = i

            if words[i] not in dic:
                dic[words[i]] = i

            if dic[ord(pattern[i])] != dic[words[i]]:
                return False

        return True

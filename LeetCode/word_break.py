from typing import List
class Solution:
    def wordBreak(self, word: str, wordDict: [str]):

        def dfs(curWord: str, index: int):
            result = 0
            if curWord !=word[:index] or len(curWord) > len(word) or index > len(word):
                return 0

            if curWord == word:
                return 1

            for w in wordDict:
                if w.startswith(word[index]):
                    result += dfs(curWord + w, index + len(w))
            return result

        answer = dfs('', 0)
        return True if answer > 0 else False


if __name__ == '__main__':
    sol = Solution()
    s = 'cars'
    wordDict = ['car', 'ca', 'rs']
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # s = 'aaaaaaa'
    # wordDict = ['aaa', 'aaaa']
    s = "ccbb"
    wordDict = ["bc", "cb"]
    print(sol.wordBreak(s, wordDict))
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dp = {word: {} for word in wordList}

        dist = {x: self.countDiff(beginWord, x) for x in wordList}
        for start in wordList:
            for end in wordList:
                if start == end:
                    dp[start][end] = 0
                else:
                    dp[start][end] = 1 if self.countDiff(start, end) == 1 else float('inf')

        q = deque([word for word in dist if dist[word] == 1])
        visited = [word for word in dist if dist[word] == 1]
        while q:
            nextWord = q.popleft()
            for word in dp[nextWord]:
                if word not in visited and dp[nextWord][word] == 1:
                    dist[word] = min(dist[word], dist[nextWord] + dp[nextWord][word])
                    visited.append(word)
                    q.append(word)
        print(dist)
        return 1

    def countDiff(self, left: str, right: str):
        count = 0
        n = len(left)
        for i in range(n):
            if left[i] != right[i]:
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    sol.ladderLength("hit", "cog",  ["hot","dot","dog","lot","log","cog"])
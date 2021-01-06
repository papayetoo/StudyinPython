class Solution:
    def partition(self, s):
        res = []
        # self.dfs(s, [], res)
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        self.dfs2(s, 0, [], dp, res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)

    def dfs2(self, s, st, path, dp, res):
        if st >= len(s):
            res.append(path)
            return
        for end in range(st, len(s)):
            if s[st] == s[end] and (end - st <= 2 or dp[st+1][end-1]):
                dp[st][end] = True
                path.append(s[st:end-st+1])
                self.dfs2(s[st+1:end], end+1, path, dp, res)
                path.pop()

    def isPal(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.partition("cdd"))
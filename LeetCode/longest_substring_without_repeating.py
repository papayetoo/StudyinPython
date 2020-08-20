from string import ascii_lowercase


class Solution:
    answer = 0

    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        for c in s:
            if c not in chars:
                chars[c] = 1
            else:
                chars[c] += 1
        visited = []
        chars = [key for key in chars if chars[key] > 0]
        if ''.join(chars) in s:
            return len(chars)
        longest_word = ''

        def dfs(output: str):
            if output in s and output != '':
                nonlocal longest_word
                if len(longest_word) < len(output):
                    longest_word = output

            if len(output) == len(chars):
                return

            for c in chars:
                if c not in visited:
                    visited.append(c)
                    dfs(output + c)
                    visited.pop()

        dfs('')
        return len(longest_word)

    def lengthOfLongestSubstring2(self, s: str) -> int:
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            # when char already in dictionary
            if ch in dic:
                # check length from start of string to index
                res = max(res, i - start)
                # update start of string index to the next index
                start = max(start, dic[ch] + 1)
            # add/update char to/of dictionary
            dic[ch] = i
        # answer is either in the begining/middle OR some mid to the end of string
        return max(res, len(s) - start)


if __name__ == '__main__':
    s = "xrstenkqqpj"
    # s = "bbbbb"
    s = "pwwkew"
    sol = Solution()
    print(sol.lengthOfLongestSubstring2(s))

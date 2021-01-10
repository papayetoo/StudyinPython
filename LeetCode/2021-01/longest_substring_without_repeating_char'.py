class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        ans = set()
        n = len(s)
        left = right = 0
        longest = 0
        while left < n and right < n:
            if s[right] not in ans:
                ans.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                ans.remove(s[left])
                left += 1
        print(longest)
        return longest


if __name__ == "__main__":
    word = "pwwkew"
    # word = "dvdf"
    sol = Solution()
    sol.lengthOfLongestSubstring(word)

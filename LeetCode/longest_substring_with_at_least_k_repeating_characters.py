from collections import defaultdict, Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        counter = Counter(s)
        includes = [x for x in counter if counter[x] >= k]
        notIncludes = [x for x in counter if counter[x] < k]
        left = 0
        right = n - 1
        while left <= right:
            temp = s[left:right + 1]
            tc = Counter(temp)

            less = [x for x in tc if tc[x] < k]
            # In = [x for x in tc if x in notIncludes]

            if len([x for x in tc if tc[x] >= k]) == len(set(temp)):
                print(temp)
                break

            if s[left] in notIncludes:
                left += 1
                continue
            if s[right] in notIncludes:
                right -= 1
                continue

            if s[left] in includes and s[left] in less:
                left += 1
                continue
            if s[right] in includes and s[right] in less:
                right -= 1
                continue

        return 0






if __name__ == '__main__':
    sol = Solution()
    s = "bbaaacbd"
    k = 3
    sol.longestSubstring(s, k)

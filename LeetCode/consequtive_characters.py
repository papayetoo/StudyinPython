from itertools import groupby


class Solution:
    def maxPower(self, s: str) -> int:
        answer = 0
        for key, count in groupby(s):
            answer = max(answer, len(list(count)))
        print(answer)
        return answer


if __name__ == "__main__":
    Solution().maxPower('leetcode')

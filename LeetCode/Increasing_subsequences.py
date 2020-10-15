from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        answer = []
        n = len(nums)

        def dfs(idx: int, res: list):
            nonlocal answer
            if idx >= n:
                return

            if len(res) > 1 and res not in answer:
                answer.append(res)

            for i in range(idx + 1, len(nums)):
                if nums[i] >= nums[idx]:
                    dfs(i, res + [nums[i]])

        for i in range(n-1):
            dfs(i, [nums[i]])
        print(answer)
        return None


if __name__ == "__main__":
    nums = [4, 6, 7, 7]
    nums = [1,2,3,1,2,3]
    sol = Solution()
    sol.findSubsequences(nums)

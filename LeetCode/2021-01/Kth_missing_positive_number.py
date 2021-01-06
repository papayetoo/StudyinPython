from typing import List


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        curr = 1
        answer = []

        while curr < arr[-1]:
            if curr not in arr:
                answer.append(curr)
            curr += 1

        return answer[k - 1] if len(answer) >= k else curr + k - len(answer)

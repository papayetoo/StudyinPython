from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 실패한 코드
        # 비교 과정이 많아서 마지막 테스트 케이스에서 TLE 걸림.
        n = len(nums)

        if k == 1:
            return nums
        if k == n:
            return [max(nums)]

        queue = deque(nums[:k])
        result = []
        pos = None
        for i in range(n - k + 1):
            if len(queue) < k:
                queue.append(nums[i + k - 1])

            if len(result) == 0:
                result.append(max(queue))
                pos = queue.index(max(queue))
            else:
                if pos == 0 and result[-1] < queue[-1]:
                    result.append(queue[-1])
                    pos = k - 1
                elif 0 < pos < k:
                    if result[-1] > queue[-1]:
                        result.append(result[-1])
                        pos -= 1
                    else:
                        result.append(queue[-1])
                        pos = k - 1
                else:
                    result.append(max(queue))
                    pos = queue.index(max(queue))
            queue.popleft()
        return result

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        # 슬라이딩 윈도우 이용하여 성공한 코드.
        # 속도 개선 가능할 듯하므로 더 탐색 필요.
        queue = deque()
        n = len(nums)
        result = []

        for i in range(k):

            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        result.append(nums[queue[0]])

        for i in range(k, n):

            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            if queue and abs(queue[0] - i) >= k:
                queue.popleft()
            queue.append(i)
            result.append(nums[queue[0]])

        return result


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # nums = [7,2,4]
    k = 2
    sol = Solution()
    answer = sol.maxSlidingWindow(nums, k)
    print(answer)

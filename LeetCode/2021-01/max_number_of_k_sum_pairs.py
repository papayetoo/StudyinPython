from collections import Counter
from typing import List


class Solution:
    # 딕셔너리를 활용한 문제라고 생각됨.
    # TLE를 해결하기 위해서 1부터 차례로 증가하는 게 아니라
    # nums에 포함된 수만을 진행하는 게 시간 초과를 방지함.
    def maxOperations(self, nums: List[int], k: int) -> int:
        half = k // 2
        counter = Counter(nums)
        if sum(nums) < k:
            return 0
        answer = 0
        keys = set(nums)
        for i in keys:
            if k - i in counter and i != k - i:
                temp = min(counter[i], counter[k - i])
                answer += temp
                counter[i] -= temp
                counter[k - i] -= temp
                continue
            if i == k - i:
                answer += counter[i] // 2
                counter[i] //= 2
                continue
        return answer

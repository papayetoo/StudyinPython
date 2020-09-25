from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        newNums = list(map(str, nums))

        class Predicate(str):
            def __lt__(self, other):
                return self + other < other + self

        newNums.sort(key=Predicate, reverse=True)
        return ''.join(newNums) if newNums[0] != '0' else '0'
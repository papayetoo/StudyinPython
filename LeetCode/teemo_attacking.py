from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        if len(timeSeries) == 0:
            return 0

        curSt = timeSeries[0]
        curEnd = timeSeries[0] + duration - 1
        answer = 0

        for i in range(1, len(timeSeries)):
            if timeSeries[i] <= curEnd:
                curEnd = timeSeries[i] + duration - 1
            else:
                answer += curEnd - curSt + 1
                curSt = timeSeries[i]
                curEnd = timeSeries[i] + duration - 1
        answer += curEnd - curSt + 1
        return answer

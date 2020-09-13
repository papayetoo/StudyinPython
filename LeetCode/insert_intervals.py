from typing import List
import bisect


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        endTimes = [y for (x, y) in intervals]

        insertPos = bisect.bisect_left(endTimes, newInterval[0])
        i = insertPos

        nStart = newInterval[0]
        nEnd = newInterval[1]
        while i < len(intervals) and intervals[i][0] < newInterval[1]:
            nStart = min(nStart, intervals[i][0])
            nEnd = max(nEnd, intervals[i][1])
            i += 1

        answerIntervals = intervals[:insertPos] + [[nStart, nEnd]] + intervals[i:]
        return answerIntervals


if __name__ == '__main__':
    s = Solution()
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(s.insert(intervals,newInterval))
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(s.insert(intervals,newInterval))
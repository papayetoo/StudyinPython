from typing import List
import bisect


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        endX = [y for (x, y) in intervals]

        beginPos = bisect.bisect_left(endX, newInterval[0])
        i = beginPos

        newMinX = newInterval[0]
        newMaxX = newInterval[1]
        while i < len(intervals) and intervals[i][0] < newInterval[1]:
            newMinX = min(newMinX, intervals[i][0])
            newMaxX = max(newMaxX, intervals[i][1])
            i += 1

        answerIntervals = intervals[:beginPos] + [[newMinX, newMaxX]] + intervals[i:]
        return answerIntervals


if __name__ == '__main__':
    s = Solution()
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(s.insert(intervals,newInterval))
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(s.insert(intervals,newInterval))
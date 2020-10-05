from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        answer = n
        tmp = []
        intervals.sort(key=lambda x: (x[0], -x[1]))
        i = 0
        while i < n:
            curSt, curEnd = intervals[i]
            # for j in range(i + 1, n):
            #     st, end = intervals[j]
            #     if curSt <= st and curEnd >= end:
            #         continue
            #     else:
            #         break
            j = i + 1
            while j < n:
                st, end = intervals[j]
                if curSt <= st and curEnd >= end:
                    j += 1
                else:
                    break
            i = j
            tmp.append([curSt, curEnd])
        return len(tmp)


if __name__ == '__main__':
    # intervals = [[1,4],[3,6],[2,8]]
    intervals = [[1,2],[1,4],[3,4]]
    # intervals = [[0,10],[5,12]]
    # intervals = [[1,4], [2,3]]
    s = Solution()
    answer = s.removeCoveredIntervals(intervals)
    print(answer)
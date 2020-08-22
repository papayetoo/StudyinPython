import bisect
import random
from typing import List

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        npts = [(r[2] - r[0] + 1) * (r[3] - r[1] + 1) for r in self.rects]
        self.preSum = [0] * len(rects)
        self.preSum[0] = npts[0]
        for i in range(1, len(npts)):
            self.preSum[i] = self.preSum[i - 1] + npts[i]
        self.total = self.preSum[-1]

    def pickRect(self):
        rand = random.randint(0, self.total - 1)
        return bisect.bisect_right(self.preSum, rand)

    def pickPoint(self, n: int):
        rect = self.rects[n]
        x1, y1 = rect[0], rect[1]
        x2, y2 = rect[2], rect[3]
        return [random.randint(x1, x2), random.randint(y1, y2)]

    def pick(self) -> List[int]:
        pickedRect = self.pickRect()
        return self.pickPoint(pickedRect)

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
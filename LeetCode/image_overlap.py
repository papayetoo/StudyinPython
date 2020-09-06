from typing import List
from itertools import product
from collections import defaultdict

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]):
        posA = [(r, c) for r in range(len(A)) for c in range(len(A)) if A[r][c] == 1]
        posB = [(r, c) for r in range(len(B)) for c in range(len(B)) if B[r][c] == 1]
        ans = 0
        trans = defaultdict(int)
        for pa in posA:
            for pb in posB:
                vec = (pb[0] - pa[0], pb[1] - pa[1])
                trans[vec] += 1
                ans = max(ans, trans[vec])

        return ans


if __name__ == '__main__':
    s = Solution()
    A = [[1, 1, 0],
         [0, 1, 0],
         [0, 1, 0]]
    B = [[0, 0, 0],
         [0, 1, 1],
         [0, 0, 1]]
    print(s.largestOverlap(A, B))

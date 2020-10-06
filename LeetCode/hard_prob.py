from collections import Counter
from typing import List

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        answer = []
        for a in range(n):
            count = K
            b = a + 1
            c = a
            res = [A[c]]
            while c < n - 2:
                if count == 0 and not A[b] in res:
                    break

                if count >= 0 and A[b] in res:
                    c += 1
                    b += 1

                if count > 0 and A[b] not in res:
                    count -= 1
                    c += 1
                    b += 1
                res.append(res[-1] + A[b])
            answer.append(res)
        print(answer)
        return 0


if __name__ == '__main__':
    A = [1,2,1,2,3]
    k = 2
    s = Solution()
    s.subarraysWithKDistinct(A, k)
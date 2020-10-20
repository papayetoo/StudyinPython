from typing import List
from collections import Counter


# 가장 많은 걸 센 다음에 바꾼다.
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        ca = Counter(A)
        cb = Counter(B)
        n = len(A)

        union = [x for x in ca if x in cb]
        if len(union) == 0:
            return -1

        answer = float('inf')
        for elem in union:
            swapCount = 0
            if ca[elem] > cb[elem]:
                for i in range(n):
                    if A[i] == elem:
                        continue
                    else:
                        if B[i] == elem:
                            swapCount += 1
                        else:
                            break
                if i == n - 1:
                    answer = min(answer, swapCount)
            else:
                for i in range(n):
                    if B[i] == elem:
                        continue
                    else:
                        if A[i] == elem:
                            swapCount += 1
                        else:
                            break
                if i == n - 1:
                    answer = min(answer, swapCount)
        return answer
        # answer = float('inf')
        # for a in ca:
        #     swapCount = 0
        #     if a not in cb:
        #         continue
        #
        #     for i in range(n):
        #         if A[i] == a:
        #             continue
        #         else:
        #             if B[i] == a:
        #                 swapCount += 1
        #             else:
        #                 break
        #     if i == n - 1:
        #         answer = min(answer, swapCount)
        #
        # for b in cb:
        #     swapCount = 0
        #     if b not in ca:
        #         continue
        #
        #     for i in range(n):
        #         if B[i] == b:
        #             continue
        #         else:
        #             if A[i] == b:
        #                 swapCount += 1
        #             else:
        #                 break
        #     if i == n - 1:
        #         answer = min(answer, swapCount)
        # print(answer if answer != float('inf') else -1)
        # return answer if answer != float('inf') else -1
        # return 0


if __name__ == "__main__":
    sol = Solution()
    # A = [2, 1, 2, 4, 2, 2]
    # B = [5, 2, 6, 2, 3, 2]
    # A = [3, 5, 1, 2, 3]
    # B = [3, 6, 3, 3, 4]
    # A = [2, 1]
    # B = [5, 2]
    A = [3, 2, 2, 3, 3, 3]
    B = [2, 1, 1, 2, 2, 2]
    # Edge Case A 와 B에서 rotate 할 수 없는 경우가 가장 많을 때..
    # A = [x for x in range(10 ** 4 + 1)]
    # B = [x for x in range(10 ** 4 + 1, 2 * 10 ** 4 + 1)]
    print(sol.minDominoRotations(A, B))

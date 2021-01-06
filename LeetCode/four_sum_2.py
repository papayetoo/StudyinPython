from typing import List
from collections import Counter

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # a = Counter(A)
        # b = Counter(B)
        # c = Counter(C)
        # d = Counter(D)
        answer = 0
        a = Counter(A)
        b = Counter(B)
        c = Counter(C)
        d = Counter(D)

        def helper(res: list):
            nonlocal answer
            n = len(res)
            s = sum(res)
            if n == 4 and s == 0:
                answer += a[res[0]] * b[res[1]] * c[res[2]] * d[res[3]]
                return
            if n == 0:
                for i in a:
                    res.append(i)
                    helper(res)
                    res.pop()
            if n == 1:
                for j in b:
                    res.append(j)
                    helper(res)
                    res.pop()
            if n == 2:
                for k in c:
                    res.append(k)
                    helper(res)
                    res.pop()
            if n == 3:
                for l in d:
                    if s + l == 0:
                        res.append(l)
                        helper(res)
                        res.pop()

        helper([])
        return answer


if __name__ == "__main__":
    a = [1, 2]
    b = [-2, -1]
    c = [-1, 2]
    d =[0, 2]
    sol = Solution()
    print(sol.fourSumCount(a,b,c,d))
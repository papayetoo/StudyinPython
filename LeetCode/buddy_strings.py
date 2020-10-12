from collections import Counter

class Solution:
    def buddyString(self, A: str, B: str) -> bool:
        na, nb = len(A), len(B)
        sa, sb = set(A), set(B)

        if na != nb or sa != sb:
            return False

        diff = []
        for i in range(na):
            if A[i] != B[i]:
                diff.append(i)

        newA = list(A)
        if len(diff) == 2:
            newA[diff[0]], newA[diff[1]] = newA[diff[1]], newA[diff[0]]
            newA = ''.join(newA)
            return True if newA == B else False
        elif len(diff) == 0:
            counter = Counter(A)
            temp = [x for x in counter if counter[x] >= 2]
            return True if len(temp) > 0 else False
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    a = 'aaaaaaabc'
    b = 'aaaaaaacb'
    print(sol.buddyString(a,b))
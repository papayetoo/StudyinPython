# Next_permutation
class Solution:
    def nextGreaterElement(self, n : int):
        limit32 = 2**31 - 1
        s = list(str(n))
        n = len(s)
        ind = n - 2

        # Finding first element from right side which is smaller than next element
        # 1 3 2
        while ind >= 0 and s[ind] >= s[ind+1]:
            ind -= 1
        if ind < 0:
            return -1

        # Find first element from right side which is greater than element s[ind]
        for i in range(n-1, ind, -1):
            if s[i] > s[ind]:
                s[ind], s[i] = s[i], s[ind]
                break

        # Reversing from ind + 1 to n to make smallest number with fixed prefix
        s[ind+1:] = s[ind+1:][::-1]

        ret = int(''.join(s))
        if ret > limit32: return -1
        return ret

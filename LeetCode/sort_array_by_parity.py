class Solution:
    def sortArrayByParity(self, A:[int]) -> [int]:
        return [x for x in A if x % 2 == 0] + [x for x in A if x % 2 ==1]

    def sortArrayByParity2(self, A:[int]) -> [int]:
        A.sort(key=lambda x: x % 2)
        return A

    def sortArrayByParity3(self, A:[int]) -> [int]:
        left = 0
        right = len(A) - 1

        while left <= right:

            while left < len(A) and A[left] % 2 == 0:
                left += 1
            while right >= 0 and A[right] % 2 == 1:
                right -=1

            if left >= right:
                break

            A[left], A[right] = A[right], A[left]

        return A


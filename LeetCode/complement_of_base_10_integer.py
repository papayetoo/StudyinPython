class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # binary = bin(N)
        answer = ''
        for x in f'{N:b}':
            if x == '1':
                answer += '0'
            else:
                answer += '1'
        return int(answer, 2)


if __name__ == '__main__':
    s = Solution()
    s.bitwiseComplement(5)
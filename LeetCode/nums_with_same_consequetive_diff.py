class Solution:

    def isValid(self, number:int, K:int) -> bool:
        number_str = str(number)
        for i in range(1, len(number_str)):
            diff = abs(int(number_str[i]) - int(number_str[i-1]))
            if diff != K:
                return False
        return True

    def numsSameConsecDiff(self, N:int, K:int):
        # BFS 방식과 DFS 방식 모두 존재하는 데
        # 이해하는 데는 BFS 방식이 좀 더 잘 이해됨.
        if N == 1:
            return [i for i in range(10)]

        queue = [digit for digit in range(1, 10)]

        for level in range(N-1):
            next_queue = []
            for num in queue:
                tail_digit = num % 10
                next_digits = set([tail_digit + K, tail_digit - K])

                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_num = num * 10 + next_digit
                        next_queue.append(new_num)
            queue = next_queue

        return queue

if __name__ == '__main__':
    N, K = map(int, input().split())
    s = Solution()
    s.numsSameConsecDiff(N, K)
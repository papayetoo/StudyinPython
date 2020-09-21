from collections import deque


class Solution:
    def racecar(self, target: int) -> int:

        def bfs(mov: int, pos: int, vel: int):
            queue = deque()
            queue.append((mov, pos, vel))

            while queue:
                m, p, v = queue.popleft()
                if p == target:
                    return m

                queue.append((m + 1, p + v, v * 2))
                if (p > target and v > 0) or (p < target and v < 0) or (p + v > target and v > 0) or (
                        p + v < target and v < 0):
                    queue.append((m + 1, p, -1 if v > 0 else 1))

        answer = bfs(0, 0, 1)
        return answer


if __name__ == '__main__':
    s = Solution()
    target = 4
    print(s.racecar(target))

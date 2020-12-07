from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            arr[0][i] = i + 1

        def helper(sty: int, stx, dy: int, dx: int, move: int, num: int):
            nonlocal arr
            for i in range(move):
                arr[sty + dy][stx + dx] = num
                num += 1
                sty += dy
                stx += dx
            return sty, stx, num

        y = [1, 0, -1, 0]
        x = [0, -1, 0, 1]
        count = 0
        nnum = arr[0][-1] + 1
        move = n - 1
        ny = 0
        nx = n - 1

        while nnum < n ** 2:
            ny, nx, nnum = helper(ny, nx, y[count % 4], x[count % 4], move, nnum)
            ny, nx, nnum = helper(ny, nx, y[(count + 1) % 4], x[(count + 1) % 4], move, nnum)
            count += 2
            move -= 1

        # for line in arr:
        #     print(line)
        return arr


if __name__ == "__main__":
    sol = Solution()
    sol.generateMatrix(5)
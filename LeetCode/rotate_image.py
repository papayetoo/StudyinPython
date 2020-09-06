from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix) // 2):
            matrix[r], matrix[len(matrix) - r - 1] = matrix[len(matrix) - r - 1], matrix[r]

        visited = []
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if r != c and (r, c) not in visited:
                    visited.append((r, c))
                    visited.append((c, r))
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        print(matrix)

    def rotate2(self, matrix: List[List[int]]) -> None:
        matrix = [[col for col in row] for row in zip(*matrix)]
        for r in matrix:
            r.reverse()
        print(matrix)


if __name__ == '__main__':
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s = Solution()
    s.rotate(arr)

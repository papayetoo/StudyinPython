from typing import List
# 행렬을 대각선 방향으로 정렬한 행렬을 반환하라는 문제.

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        answers = [[0 for _ in range(cols)] for _ in range(rows)]
        start_points = [(0, x) for x in range(cols)]
        for row in range(1, rows):
            start_points.append((row, 0))

        for start_point in start_points:
            row, col = start_point
            points = []
            values = []
            while row < rows and col < cols:
                points.append((row, col))
                values.append(mat[row][col])
                row += 1
                col += 1
            values.sort()
            for idx, point in enumerate(points):
                answers[point[0]][point[1]] = values[idx]
        return answers

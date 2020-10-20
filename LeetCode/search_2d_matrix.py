from colletions import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if not rows:
            return False

        for r in range(rows):
            if target in matrix[r]:
                return True
        return False

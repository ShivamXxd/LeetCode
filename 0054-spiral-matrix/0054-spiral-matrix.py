from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self._spiralOrderHelper(matrix, [])

    def _spiralOrderHelper(self, matrix: List[List[int]], result: List[int]) -> List[int]:
        if not matrix or not matrix[0]:
            return result
        row = len(matrix)
        col = len(matrix[0])
        if row == 1:
            result += matrix[0]
            return result
        if col == 1:
            for r in matrix:
                result.append(r[0])
            return result
        result += matrix[0]
        for i in range(1, row - 1):
            result.append(matrix[i][col - 1])
        result += matrix[row - 1][::-1]
        for i in range(row - 2, 0, -1):
            result.append(matrix[i][0])
        newMatrix = [r[1:-1] for r in matrix[1:-1]]
        return self._spiralOrderHelper(newMatrix, result)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        zeros = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zeros.add((i, j))
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0 and (i, j) in zeros:
                    for r in range(row):
                        matrix[r][j] = 0
                    for c in range(col):
                        matrix[i][c] = 0

        
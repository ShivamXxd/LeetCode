class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        row = len(mat[0])
        for i in range(row):
            for j in range(row):
                if i == j:
                    total += mat[i][j]
            total += mat[i][row - 1 - i]
        if len(mat) % 2 != 0:
            total -= mat[row // 2][row // 2]
        return total
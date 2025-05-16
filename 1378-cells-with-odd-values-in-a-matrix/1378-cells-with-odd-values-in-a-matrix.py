class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [[0]*n for _ in range(m)]
        count = 0
        for i in range(len(indices)):
            for j in range(n):
                mat[indices[i][0]][j] += 1
            for j in range(m):
                mat[j][indices[i][1]] += 1
            print(mat)
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] % 2 == 1:
                    count += 1
        return count
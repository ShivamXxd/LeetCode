class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            start = 0
            end = len(matrix[i]) - 1
            if target <= matrix[i][-1]:
                while start <= end:
                    mid = end + (start - end) // 2
                    if target == matrix[i][mid]:
                        return True
                    elif target > matrix[i][mid]:
                        start = mid + 1
                    elif target < matrix[i][mid]:
                        end = mid - 1
        return False
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)  # Add a sentinel

            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)

            heights.pop()
            return max_area

        n = len(matrix[0])
        heights = [0] * n
        max_rect = 0

        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            max_rect = max(max_rect, largestRectangleArea(heights))

        return max_rect


        # O(m^2 * n^2) Time complexity, exceeds time limit for 1 test case.
        # matrix = [[int(cell) for cell in row] for row in matrix]
        # row = len(matrix)
        # col = len(matrix[0])
        # max_area = 0
        # for i in range(row):
        #     for j in range(col):
        #         if matrix[i][j] == 1:
        #             length = col
        #             breadth = 0
        #             for r in range(i, row):
        #                 if matrix[r][j] == 0:
        #                     break
        #                 width = 0
        #                 for c in range(j, col):
        #                     if matrix[r][c] == 1:
        #                         width += 1
        #                     else:
        #                         break
        #                 length = min(length, width)
        #                 breadth += 1
        #                 max_area = max(max_area, length * breadth)
        # return max_area
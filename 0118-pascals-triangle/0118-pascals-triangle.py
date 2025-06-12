class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):  # till all rows are done
            row = [1] * (i + 1)   # create dummy row
            # the below loop doesn't run for i = 0
            for j in range(1, i): # start and end will always be 1 so we change the middle elements only
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j] # update the row with last row's j-1 and j being added to make new j
            triangle.append(row) # append the generated row
        return triangle

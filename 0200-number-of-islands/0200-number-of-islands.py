class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
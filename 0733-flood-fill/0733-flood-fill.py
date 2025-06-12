class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])

        target = image[sr][sc]

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return 
            if image[r][c] != target or image[r][c] == color:
                return
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        dfs(sr, sc)
        return image
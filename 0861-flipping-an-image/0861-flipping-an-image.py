class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row = len(image)
        col = len(image[0])

        for i in range(row):
            # for j in range(col // 2):
            #     image[i][j], image[i][col-j-1] = image[i][col-j-1], image[i][j]
            image[i] = image[i][::-1]
        
        for i in range(row):
            for j in range(col):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        
        return image
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # candies = 0
        # if ratings[0] > ratings[1]:
        #     candies += 2
        # else: candies += 1
        # if ratings[len(ratings) - 1] > ratings[len(ratings) - 2]:
        #     candies += 2
        # else: candies += 1
        # for i in range(len(ratings)):
        #     if i >= 1 and i < len(ratings) - 1:
        #         if ratings[i] > ratings[i - 1] or ratings[i] > ratings[i+1]:
        #             candies += 2
        #         # elif ratings[i] > ratings[i+1]:
        #         #     candies += 2
        #         else: 
        #             candies += 1
        # return candies
        n = len(ratings)
        candies = [1] * n

        count = 0

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i] + 1, candies[i - 1])
            count += candies[i - 1]
        return count + candies[n - 1]

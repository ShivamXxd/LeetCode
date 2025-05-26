class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        position = n - 1

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                result[position] = left_square
                left += 1
            else:
                result[position] = right_square
                right -= 1
            position -= 1
        return result
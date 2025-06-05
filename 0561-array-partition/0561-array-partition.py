class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        total = 0
        for i in range(len(nums)-2, -1, -2):
            total += nums[i]
        return total
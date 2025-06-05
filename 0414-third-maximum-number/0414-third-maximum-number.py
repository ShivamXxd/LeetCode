class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums = sorted(nums)
        print(nums)
        if len(nums) >= 3:
            return nums[-3]
        else:
            return nums[-1]
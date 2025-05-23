class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = [str(x) for x in nums]
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        result = ''.join(map(str, nums)).lstrip('0') or '0'
        return result


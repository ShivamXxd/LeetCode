class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # prefix = [1] * n
        # # high time complexity O(n^2)
        # for i in range(n):
        #     for j in range(n):
        #         if j == i:
        #             continue
        #         else:
        #             prefix[i] *= nums[j]

        # return prefix
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

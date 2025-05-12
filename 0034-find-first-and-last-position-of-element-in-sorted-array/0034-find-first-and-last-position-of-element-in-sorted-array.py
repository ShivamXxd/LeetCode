class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        first = -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                first = mid
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
        last = -1
        start1 = 0
        end1 = len(nums) - 1
        while start1 <= end1:
            mid = start1 + (end1 - start1) // 2
            if nums[mid] == target:
                last = mid
                start1 = mid + 1
            elif target > nums[mid]:
                start1 = mid + 1
            elif target < nums[mid]:
                end1 = mid - 1
        return [first, last]
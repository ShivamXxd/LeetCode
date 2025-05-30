class Solution(object):
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

nums1 = [2, 0, 2, 1, 1, 0]
solution = Solution()
solution.sortColors(nums1)
print(nums1)  

nums2 = [2, 0, 1]
solution.sortColors(nums2)
print(nums2)  

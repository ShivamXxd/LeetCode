class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # left = 0
        # current_sum = sum(nums[0:k])
        # max_average = current_sum/k
        # for right in range(k, len(nums)):
        #     current_sum = (current_sum + nums[right] - nums[left])
        #     max_average = max(max_average, current_sum / k)
        #     left += 1

        # return max_average
        window_sum = sum(nums[0:k])
        max_average = window_sum / k

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_average = max(max_average, window_sum / k)
        
        return max_average
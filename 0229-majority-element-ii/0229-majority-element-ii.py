class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        result = []
        threshold = len(nums) // 3
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for num in freq:
            if freq[num] > threshold:
                result.append(num)
        return result

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        record = {}
        for i in nums:
            if i not in record:
                record[i] = 1
            else:
                record[i] += 1
        return max(record, key=record.get)
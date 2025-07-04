class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

        # record = {}
        # for i in nums:
        #     if i not in record:
        #         record[i] = 1
        #     else:
        #         record[i] += 1
        # return max(record, key=record.get)
        

        # nums.sort()
        # return nums[len(nums) // 2]
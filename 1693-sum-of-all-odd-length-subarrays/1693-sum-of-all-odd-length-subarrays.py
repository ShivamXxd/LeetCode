class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)  # create a dummy prefix array for storing sums of elements till their range

        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]  # store sums for all lengths in array arr
        
        total = 0
        for i in range(n):
            for j in range(i, n):
                if (j - i + 1) % 2 == 1:  # check for odd length subarrays 
                    total += prefix[j + 1] - prefix[i]  # add the sum of all elements in the subarray using prefix sum into total
        
        return total
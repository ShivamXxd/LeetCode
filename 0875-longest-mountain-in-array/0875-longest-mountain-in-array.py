class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        low = 0

        while low < n - 2:
            mid = low + 1
            high = mid + 1
            if arr[low] < arr[mid]:
                while mid < n - 1 and arr[mid] < arr[mid + 1]:
                    mid += 1
                high = mid
                if high < n - 1 and arr[high] > arr[high + 1]:
                    while high < n - 1 and arr[high] > arr[high + 1]:
                        high += 1
                    res = max(res, high - low + 1)
                low = high
            else:
                low += 1
        return res

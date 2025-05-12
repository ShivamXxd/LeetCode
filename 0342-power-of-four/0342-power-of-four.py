class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        # return (n & (n - 1)) == 0 and (n - 1) % 3 == 0
        if n == 1:
            return True
        if n <= 0 or n % 4 != 0:
            return False
        return self.isPowerOfFour(n // 4)
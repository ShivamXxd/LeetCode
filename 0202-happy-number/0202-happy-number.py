class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        if n < 10:
            return False
        total = 0
        while n > 0:
            rem = n % 10
            n = n // 10
            total += rem * rem
        return self.isHappy(total)
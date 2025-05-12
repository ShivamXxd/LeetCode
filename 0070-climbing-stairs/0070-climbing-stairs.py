class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        current = 0
        first = 2
        second = 3
        for _ in range(3, n):
            current = first + second
            first = second
            second = current
        return current

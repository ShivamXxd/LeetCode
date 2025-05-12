class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        current = 0
        first = 0
        second = 1
        for _ in range(1, n):
            current = first + second
            first = second
            second = current
        return current
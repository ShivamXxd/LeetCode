class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        if 1 <= n <= 3:
            return n
        memo[1] = 1
        memo[2] = 2
        memo[3] = 3
        for i in range(4, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n]

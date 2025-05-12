class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize memoization array
        memo = [0] * (n + 1)

        # Base cases
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # Set base cases in the memo array
        memo[1] = 1
        memo[2] = 2

        # Calculate the number of ways to climb stairs iteratively
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n]

# Test the function with an example
sol = Solution()
sol.climbStairs(5)  # Example input

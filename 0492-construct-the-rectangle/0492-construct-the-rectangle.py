class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        import math
        n = area
        min_diff = n  # initialize with a large difference
        result = (1, n)
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                j = n // i
                if abs(i - j) < min_diff:
                    min_diff = abs(i - j)
                    result = (i, j)
        return result[::-1]
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        count = 0
        max_depth = 0
        for i in s:
            if i == '(':
                count += 1
                max_depth = max(max_depth, count)
            elif i == ')':
                count -= 1
        return max_depth
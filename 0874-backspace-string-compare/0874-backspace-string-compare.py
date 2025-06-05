class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []       
        for i in range(len(s)):
            stack.append(s[i])
            if s[i] == '#':
                stack.pop()
                if stack:
                    stack.pop()
        result1 = ''.join(stack)
        stack = []
        for i in range(len(t)):
            stack.append(t[i])
            if t[i] == '#':
                stack.pop()
                if stack:
                    stack.pop()
        result2 = ''.join(stack)
        return result1 == result2

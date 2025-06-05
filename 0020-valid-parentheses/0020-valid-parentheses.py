class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(stack) == 1:
            return False
        for i in s:
            if i == '{' or i == '(' or i == '[':
                stack.append(i)
            elif i == '}' or i == ')' or i == ']':
                stack.append(i)
                if len(stack) > 1: 
                    if stack[-2] == '(' and stack[-1] == ')':
                        stack.pop()
                        stack.pop()
                    elif stack[-2] == '{' and stack[-1] == '}':
                        stack.pop()
                        stack.pop()
                    elif stack[-2] == '[' and stack[-1] == ']':
                        stack.pop()
                        stack.pop()
        return len(stack) == 0
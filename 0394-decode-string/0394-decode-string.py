class Solution:
    def decodeString(self, s: str) -> str:
        # stack = []
        # repeat = 0
        # result = ""
        # for i in range(len(s)):
        #     if s[i] == '[':
        #         repeat = int(s[i-1])
        #         stack.append(s[i])
        #     elif s[i] == ']':
        #         addition = ""
        #         while stack[-1] != '[':
        #             addition += stack.pop()
        #         stack.pop()
        #         result += repeat * addition[::-1]
        #     elif not s[i].isdigit():
        #         stack.append(s[i])
        # add = ""
        # while stack:
        #     add += stack.pop()
        # result += add[::-1]
        # return result

        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                addition = ""
                while stack[-1] != '[':
                    addition = stack.pop() + addition
                stack.pop()
                repeat = ""
                while stack and stack[-1].isdigit():
                    repeat = stack.pop() + repeat
                stack.append(int(repeat) * addition)
                
        return ''.join(stack)
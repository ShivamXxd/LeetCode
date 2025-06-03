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
                stack.append(i) # add all except ]
            else:
                addition = ""  # substring to be added which will be repeated as required
                while stack[-1] != '[':
                    addition = stack.pop() + addition # reverse adding so characters would be left to right
                stack.pop()  # remove [
                repeat = ""  # how many times we neeed to repeat can be multiple digit number, convert it fully to int
                while stack and stack[-1].isdigit():
                    repeat = stack.pop() + repeat # repeat will be the full number ex: "100"
                stack.append(int(repeat) * addition) # append the required sequence in stack repeated requied number of times.

        return ''.join(stack) # join everything to make the result string
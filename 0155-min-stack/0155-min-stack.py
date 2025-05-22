class MinStack:
    def __init__(self):
        self.high = -1
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.high += 1

    def pop(self) -> None:
        if self.high < 0:
            return
        self.stack.pop()
        self.high -= 1

    def top(self) -> int:
        if self.high < 0:
            return
        return self.stack[self.high]

    def getMin(self) -> int:
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
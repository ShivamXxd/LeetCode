class MyCircularQueue:
    def __init__(self, k: int):
        self.cq = [None] * k
        self.front = -1
        self.rear = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.front == self.rear == -1:
            self.front = self.rear = 0
            self.cq[self.rear] = value
            return True

        if not self.isFull():
            self.rear = (self.rear + 1) % self.size  
            self.cq[self.rear] = value
            return True
        return False

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
            return True

        self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.cq[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.cq[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
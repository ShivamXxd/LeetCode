from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()
        for i in range(1, n + 1):
            queue.append(i)
        while len(queue) > 1: # until we get the winner i.e a single person
            for _ in range(k-1): # pop from front and append to the rear every k-1 elements
                queue.append(queue.popleft())
            queue.popleft() # remove the loser friend
        return queue[0]
from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        time = 0
        while True:
            curr = queue.popleft()
            curr -= 1
            time += 1
            if k == 0 and curr == 0:
                return time
            if curr > 0:
                queue.append(curr)
            k -= 1
            if k < 0:
                k = len(queue) - 1

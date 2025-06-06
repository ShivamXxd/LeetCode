class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        result = 0
        for i in s:
            if i == "R":
                balance += 1
            else: balance -= 1
            if balance == 0: result += 1
        return result
class Solution:
    def addDigits(self, num: int) -> int:
        # if num < 10:
        #     return num
        # list1 = [int(x) for x in str(num)]
        # total = 0
        # for i in list1:
        #     total += i
        # return self.addDigits(total)

        if num < 10:
            return num
        digits = [int(x) for x in str(num)]
        total = sum(digits)
        while total >= 10:
            digits = [int(x) for x in str(total)]
            total = sum(digits)
        return total
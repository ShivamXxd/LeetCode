class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n < 0:
        #     x = 1 / x
        #     n = -n

        # result = 1
        # current_product = x

        # while n > 0:
        #     if n % 2 == 1:  
        #         result *= current_product
        #     current_product *= current_product 
        #     n //= 2 

        # return result

        if n == 0: return 1
        if n < 0: return 1/self.myPow(x, -n)

        half = self.myPow(x, n // 2)
        if n % 2 == 0: return half*half
        else: return x * half * half

        # return x * self.myPow(x, n // 2)

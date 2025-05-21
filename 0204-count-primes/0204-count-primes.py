class Solution:
    def countPrimes(self, n: int) -> int:
        # Sieve of Eratosthenes Method
        if n < 3:
            return 0
        sieve = [True] * n
        sieve[0] = sieve[1] = False
        for i in range(4, n, 2):
            sieve[i] = False
        for i in range(3, int(n**0.5) + 1, 2):
            if sieve[i]:
                sieve[i*i:n:i*2] = [False] * len(sieve[i*i:n:i*2])
        return sum(sieve)


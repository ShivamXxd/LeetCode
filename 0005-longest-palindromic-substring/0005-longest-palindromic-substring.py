class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        # Create n x n table that stores boolean of every range of substrings dp[i][j]
        for i in range(n):     
            dp[i][i] = True  # all single characters are palindromes

        start = 0
        max_len = 1
        
        for l in range(2, n + 1): # for remaining substrings of length >= 2
            for i in range(n - l + 1): # all substring of length l starting from index i
                j = i + l - 1  # ending index of the current substring i.e start + length - 1
                if s[i] == s[j]:  # if starting and ending characters match then we start the palindrome search
                    if l == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if l > max_len: # if there a substring of greater length then update max_len and starting index 
                            start = i
                            max_len = l

        return s[start : start + max_len]  # start + max_len is the ending index
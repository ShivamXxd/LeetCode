class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        max_length = 0
        start = 0  

        for end in range(len(s)):
            if s[end] in d and d[s[end]] >= start:
                start = d[s[end]] + 1
            d[s[end]] = end

            max_length = max(max_length, end - start + 1)
        return max_length
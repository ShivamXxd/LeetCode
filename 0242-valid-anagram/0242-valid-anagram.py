class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = "esiarntolcdugpmhbyfvkwzxjq"
        for letter in letters:
            if s.count(letter) != t.count(letter):
                return False
        return True
        
        # for i in t: # This is correct but has O(n^2) Time complexity
        #     if i not in s or s.count(i) != t.count(i):
        #         return False
        # return True
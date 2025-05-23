class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in t:
            if i not in s or s.count(i) != t.count(i):
                return False
        return True
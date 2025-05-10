class Solution:
    def minTimeToType(self, word: str) -> int:
        ptr = ord(word[0]) - 97
        total_time = min(ptr, 26 - ptr) + 1

        for i in range(1, len(word)):
            ptr = abs(ord(word[i]) - ord(word[i - 1]))
            time = min(ptr, 26 - ptr)
            total_time += time + 1
        return total_time
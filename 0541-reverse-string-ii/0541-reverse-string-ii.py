class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        for i in range(0, len(s), 2 * k):
            part1 = s[i:i+k][::-1]
            part2 = s[i+k : i+2*k]
            result += part1 + part2
        return result
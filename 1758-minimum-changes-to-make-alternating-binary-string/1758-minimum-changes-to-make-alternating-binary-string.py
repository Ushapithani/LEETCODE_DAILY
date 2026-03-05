class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] != str(i % 2):
                count += 1
        return min(count, len(s) - count)
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_len = -1

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    length = j - i - 1
                    max_len = max(max_len, length)

        return max_len
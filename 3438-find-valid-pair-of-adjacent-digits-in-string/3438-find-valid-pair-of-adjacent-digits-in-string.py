class Solution:
    def findValidPair(self, s: str) -> str:
        from collections import Counter
        c = Counter(s)
        for i in range(len(s)-1):
            if s[i] != s[i+1] and c[s[i]] == int(s[i]) and c[s[i+1]] == int(s[i+1]):
                return s[i:i+2]
        return ""
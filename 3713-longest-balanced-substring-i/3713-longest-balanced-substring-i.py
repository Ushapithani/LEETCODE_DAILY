class Solution:
    def longestBalanced(self, s: str) -> int:   
        n = len(s)
        ans = 0
        
        for i in range(n):
            freq = {}
            for j in range(i, n):
                ch = s[j]
                if ch in freq:
                    freq[ch] += 1
                else:
                    freq[ch] = 1
                
                values = list(freq.values())
                balanced = True
                for v in values:
                    if v != values[0]:
                        balanced = False
                        break
                if balanced:
                    ans = max(ans, j - i + 1)
        
        return ans
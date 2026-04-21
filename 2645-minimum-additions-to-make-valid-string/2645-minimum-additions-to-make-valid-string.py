class Solution:
    def addMinimum(self, w):
        ans = 0
        prev = 'c'
        
        for c in w:
            ans += (ord(c) - ord(prev) - 1) % 3
            prev = c
        
        return ans + (prev != 'c') + (prev == 'a')
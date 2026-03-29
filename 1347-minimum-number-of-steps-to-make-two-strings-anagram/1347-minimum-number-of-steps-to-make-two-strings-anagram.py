class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter 
        c1=Counter(s)
        c2=Counter(t)
        diff = c1-c2
        return sum(diff.values())
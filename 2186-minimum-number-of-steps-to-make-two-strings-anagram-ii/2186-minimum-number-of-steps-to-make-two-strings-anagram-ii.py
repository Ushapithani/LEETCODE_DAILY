class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        c1= Counter(s)
        c2 = Counter(t)
        diff1= c1-c2
        diff2 = c2-c1
        return sum(diff1.values())+sum(diff2.values())

        
        
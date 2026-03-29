class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff1 = []
        diff2 = []
        
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff1.append(c1)
                diff2.append(c2)
        
        if len(diff1) == 0:
            return True
        if len(diff1) == 2:
            return sorted(diff1) == sorted(diff2)
        return False
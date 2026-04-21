class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal = 0
        res = 0
        for c in s:
            if c == 'R':
                bal += 1
            else:
                bal -= 1
            if bal == 0:
                res += 1
        return res
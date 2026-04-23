class Solution:
    def countAsterisks(self, s: str) -> int:
        bars = ans = 0
        for ch in s:
            if ch == '|':
                bars += 1
            elif ch == '*' and bars % 2 == 0:
                ans += 1
        return ans
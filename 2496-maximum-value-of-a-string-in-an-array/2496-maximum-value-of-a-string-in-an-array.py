class Solution:
    def maximumValue(self, strs):
        ans = 0
        for s in strs:
            if s.isdigit():
                ans = max(ans, int(s))
            else:
                ans = max(ans, len(s))
        return ans
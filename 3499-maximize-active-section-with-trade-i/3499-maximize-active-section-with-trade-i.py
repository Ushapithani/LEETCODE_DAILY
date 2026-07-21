class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        i = 0
        ones = 0

        pre = float("-inf")
        mx = 0

        while i < n:
            j = i

            while j < n and s[j] == s[i]:
                j += 1

            cnt = j - i

            if s[i] == '1':
                ones += cnt
            else:
                mx = max(mx, pre + cnt)
                pre = cnt

            i = j

        return ones + mx
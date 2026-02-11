class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        from functools import lru_cache

        @lru_cache(None)
        def helper(i, j):
            k = i + j
            if k == len(s3):
                return True
            ans = False
            if i < len(s1) and s1[i] == s3[k]:
                ans = ans or helper(i+1, j)
            if j < len(s2) and s2[j] == s3[k]:
                ans = ans or helper(i, j+1)
            return ans

        return helper(0, 0)
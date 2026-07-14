from functools import lru_cache
from math import gcd

class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(i, g1, g2):
            if i == len(nums):
                return g1 == g2 != 0

            return (
                dfs(i + 1, g1, g2) +
                dfs(i + 1, gcd(g1, nums[i]), g2) +
                dfs(i + 1, g1, gcd(g2, nums[i]))
            ) % MOD

        return dfs(0, 0, 0)
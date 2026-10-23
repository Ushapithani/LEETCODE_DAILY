class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            bits = dp[i // 2] + (i % 2)
            dp[i] = bits
            
        return dp
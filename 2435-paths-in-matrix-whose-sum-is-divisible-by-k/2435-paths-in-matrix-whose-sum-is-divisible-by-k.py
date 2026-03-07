class Solution(object):
    def numberOfPaths(self, grid, k):
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        dp = []
        for i in range(m):
            row = []
            for j in range(n):
                inner = []
                for r in range(k):
                    inner.append(0)
                row.append(inner)
            dp.append(row)

        dp[0][0][grid[0][0] % k] = 1

        for i in range(1, m):
            for r in range(k):
                prev_r = (r - grid[i][0]) % k
                dp[i][0][r] = dp[i-1][0][prev_r]

        for j in range(1, n):
            for r in range(k):
                prev_r = (r - grid[0][j]) % k
                dp[0][j][r] = dp[0][j-1][prev_r]

        for i in range(1, m):
            for j in range(1, n):
                for r in range(k):
                    prev_r = (r - grid[i][j]) % k
                    dp[i][j][r] = (dp[i-1][j][prev_r] + dp[i][j-1][prev_r]) % MOD

        return dp[m-1][n-1][0]
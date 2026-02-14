class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured] 
        for row in range(query_row):
            next_row = [0] * (row + 2)
            for i in range(len(dp)):
                if dp[i] > 1:
                    overflow = (dp[i] - 1) / 2.0
                    next_row[i] += overflow
                    next_row[i + 1] += overflow
            dp = next_row
        return min(1, dp[query_glass])
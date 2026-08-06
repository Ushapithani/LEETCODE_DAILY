class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                diff = i-coin
                if diff >=0:
                    dp[i] = min(dp[i], dp[diff] + 1)

        if dp[amount] == amount + 1:
            return -1

        return dp[amount]
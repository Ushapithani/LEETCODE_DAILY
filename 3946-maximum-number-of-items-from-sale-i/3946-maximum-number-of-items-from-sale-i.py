
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        dp = [0] * (budget + 1)
        min_price = float('inf')

        for i in range(n):
            factor = items[i][0]
            price = items[i][1]

            min_price = min(min_price, price)

            free_count = 0

            for j in range(n):
                if i != j and items[j][0] % factor == 0:
                    free_count += 1

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + free_count + 1)

        ans = 0

        for b in range(budget + 1):
            remaining = budget - b
            total = dp[b] + remaining // min_price
            ans = max(ans, total)

        return ans

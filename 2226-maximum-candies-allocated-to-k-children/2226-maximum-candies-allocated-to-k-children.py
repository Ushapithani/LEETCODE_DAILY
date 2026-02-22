class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        left, right = 1, max(candies)

        while left < right:
            mid = (left + right + 1) // 2
            count = 0
            for pile in candies:
                count += pile // mid

            if count >= k:
                left = mid
            else:
                right = mid - 1

        return left if sum(candies) >= k else 0
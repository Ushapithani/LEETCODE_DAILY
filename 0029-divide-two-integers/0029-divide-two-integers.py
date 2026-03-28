class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = int(dividend / divisor)
        return max(-(2**31), min(2**31 - 1, ans))
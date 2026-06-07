class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = int(str(abs(x))[::-1])
        x *= sign

        if x < -2**31 or x > 2**31 - 1:
            return 0
        return x
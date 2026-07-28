class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s == 0:
            return 0

        if s > 9 * n:
            return -1

        ans = ""

        for i in range(n):
            digit = min(9, s)
            ans += str(digit)
            s -= digit

        return int(ans)
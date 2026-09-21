class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for num in range(low, high + 1):
            s = str(num)
            n = len(s)

            if n % 2 != 0:
                continue

            mid = n // 2

            left = 0
            right = 0

            for i in range(mid):
                left += int(s[i])

            for i in range(mid, n):
                right += int(s[i])

            if left == right:
                count += 1

        return count
class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = []
        count = 0

        while True:
            ans.append(str(n % 10))
            n //= 10
            count += 1

            if n == 0:
                break

            if count == 3:
                ans.append(".")
                count = 0

        return "".join(ans[::-1])
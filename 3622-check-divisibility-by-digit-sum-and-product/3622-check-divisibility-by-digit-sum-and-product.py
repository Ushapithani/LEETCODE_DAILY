class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ = 0
        prod = 1
        for i in str(n):
            summ += int(i)
            prod *= int(i)
        return True if n % (summ+prod) == 0 else False

        
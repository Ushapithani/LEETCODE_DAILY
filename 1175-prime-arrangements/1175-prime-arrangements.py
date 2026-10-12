class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime = 0

        for i in range(2, n + 1):
            is_prime = True

            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break

            if is_prime:
                prime += 1

        non_prime = n - prime

        result = 1
        for i in range(1, prime + 1):
            result *= i

        for i in range(1, non_prime + 1):
            result *= i

        return result % (10**9 + 7)
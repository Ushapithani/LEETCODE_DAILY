class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n
        pointers = [0] * len(primes)

        for i in range(1, n):
            candidates = []
            for j in range(len(primes)):
                candidates.append(ugly[pointers[j]] * primes[j])
            
            ugly[i] = min(candidates)

            for j in range(len(primes)):
                if ugly[i] == candidates[j]:
                    pointers[j] += 1

        return ugly[n - 1]
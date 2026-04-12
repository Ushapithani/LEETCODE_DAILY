class Solution:
    def minOperations(self, nums: list[int]) -> int:
        
        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            i = 3
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 2
            return True
        
        def next_prime(n):
            while not is_prime(n):
                n += 1
            return n
        
        def next_non_prime(n):
            if n < 0:
                n = 0
            while is_prime(n):
                n += 1
            return n
        
        ops = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                target = next_prime(nums[i])
            else:
                target = next_non_prime(nums[i])
            ops += target - nums[i]
        
        return ops
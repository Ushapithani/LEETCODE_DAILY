class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        total = 10
        available = 9
        unique = 9
        
        for k in range(2, n + 1):
            unique = unique * available
            total += unique
            available -= 1
        
        return total
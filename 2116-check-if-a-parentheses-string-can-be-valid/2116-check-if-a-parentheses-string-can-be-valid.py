class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        
        if n % 2 == 1:
            return False
        
        min_open = 0
        max_open = 0
        
        for i in range(n):

            if locked[i] == '0':
                min_open -= 1
                max_open += 1

            else:

                if s[i] == '(':
                    min_open += 1
                    max_open += 1
                    
                else:
                    min_open -= 1
                    max_open -= 1
            
            if max_open < 0:
                return False
            
            min_open = max(min_open, 0)
        
        return min_open == 0
class Solution:
    def minSwaps(self, s: str) -> int:
        open = 0 

        for c in s :

            if c == '[':
                open+=1

            else :

                if open > 0:
                    open -=1
                    
        return (open+1)//2
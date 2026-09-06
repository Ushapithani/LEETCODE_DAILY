class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left,right+1):
            original = num 
            valid = True 
            while num > 0 :
                digit = num%10

                if digit == 0 or original%digit!=0:
                    valid = False
                    break 
                num//=10
            if valid :
                ans.append(original)
        return ans 

        
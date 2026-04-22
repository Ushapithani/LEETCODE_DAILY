class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')
        left_zeros = 0
        right_ones = total_ones
        ans = 0
        
        for i in range(len(s) - 1):  
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1
            
            ans = max(ans, left_zeros + right_ones)
        
        return ans
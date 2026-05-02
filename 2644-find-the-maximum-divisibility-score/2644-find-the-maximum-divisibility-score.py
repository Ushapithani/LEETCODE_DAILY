class Solution:
    def maxDivScore(self, nums, divisors):
        max_count = -1
        ans = float('inf')
        
        for d in divisors:
            count = 0
            for num in nums:
                if num % d == 0:
                    count += 1
            
            if count > max_count:
                max_count = count
                ans = d
            elif count == max_count:
                ans = min(ans, d)
        
        return ans
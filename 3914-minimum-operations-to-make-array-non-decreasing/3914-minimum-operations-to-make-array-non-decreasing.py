class Solution:
    def minOperations(self, nums):
        nums_copy = nums[:]   
        
        ans = 0
        max_so_far = nums[0]
        prev_need = 0
        
        for x in nums:
            max_so_far = max(max_so_far, x)
            need = max_so_far - x
            
            if need > prev_need:
                ans += need - prev_need
            
            prev_need = need
        
        return ans
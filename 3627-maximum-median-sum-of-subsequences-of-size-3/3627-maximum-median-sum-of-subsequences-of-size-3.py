class Solution:
    def maximumMedianSum(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        n = len(nums)
        
        i = n // 2 - 1
        while i < n - 1:
            result += nums[i]
            i += 2
        
        return result
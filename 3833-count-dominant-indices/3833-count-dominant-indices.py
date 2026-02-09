from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        averages = {}
        for i in range(n-1):
            right_sum = prefix[n] - prefix[i+1]
            right_len = n - i - 1
            averages[i] = right_sum / right_len
        
        count = 0
        for i in range(n-1):
            if nums[i] > averages[i]:
                count += 1
        return count
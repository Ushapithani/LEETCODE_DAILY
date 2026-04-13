from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_distance = len(nums)  
        
        
        for i in range(len(nums)):
            if nums[i] == target:
                distance = abs(i - start)
                if distance < min_distance:
                    min_distance = distance
        
        return min_distance
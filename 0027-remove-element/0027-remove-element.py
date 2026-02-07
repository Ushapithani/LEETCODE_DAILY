class Solution:
    def removeElement(self, nums, val):
        if not nums:
            return 0
        
        unique = []
        for num in nums:
            if num != val:
                unique.append(num)
        
        for i in range(len(unique)):
            nums[i] = unique[i]
        
        return len(unique)
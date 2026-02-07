class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        unique = []
        for num in nums:
            if unique.count(num) == 0 :
                unique.append(num)
        for i in  range (len(unique)):
            nums[i] = unique[i]
        return len(unique)
class Solution:
    def findErrorNums(self, nums):
        freq = {}
        duplicate = -1
        missing = -1
        
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        n = len(nums)
        for i in range(1, n + 1):
            if i in freq:
                if freq[i] == 2:
                    duplicate = i
            else:
                missing = i
        
        return [duplicate, missing]
class Solution:
    def findShortestSubArray(self, nums):
        first = {}
        count = {}
        degree = 0
        ans = len(nums)
        
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
            if count[num] > degree:
                degree = count[num]
                ans = i - first[num] + 1
            elif count[num] == degree:
                ans = min(ans, i - first[num] + 1)
        
        return ans


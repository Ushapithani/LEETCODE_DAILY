class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)
        suf = nums[:]
        for i in range(n-2, -1, -1):
            suf[i] = min(suf[i], suf[i+1])
        
        mx = 0
        for i, x in enumerate(nums):
            mx = max(mx, x)
            if mx - suf[i] <= k:
                return i
        return -1
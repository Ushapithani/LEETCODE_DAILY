class Solution:
    def maximizeSum(self, nums, k):
        x = max(nums)
        return x * k + (k * (k - 1)) // 2
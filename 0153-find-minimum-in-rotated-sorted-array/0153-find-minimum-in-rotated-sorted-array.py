class Solution:
    def findMin(self, nums):
        unique_ele = set(nums)
        return min(unique_ele)
class Solution:
    def countElements(self, nums):
        min_val, max_val = min(nums), max(nums)
        count = 0
        for num in nums:
            if min_val < num < max_val:
                count += 1
        return count
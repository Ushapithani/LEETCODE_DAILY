class Solution:
    def countElements(self, nums):
        minimum = min(nums)
        maximum = max(nums)

        if minimum == maximum:
            return 0

        return len(nums) - nums.count(minimum) - nums.count(maximum)
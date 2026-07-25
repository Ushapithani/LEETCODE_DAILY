class Solution:
    def countElements(self, nums):
        minimum = min(nums)
        maximum = max(nums)

        count = 0

        for num in nums:
            if num != minimum and num != maximum:
                count += 1

        return count
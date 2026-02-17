class Solution:
    def numSubarrayBoundedMax(self, nums, left, right):
        def countSubarrays(maxLimit):
            total = 0
            streak = 0
            for value in nums:
                if value > maxLimit:
                    streak = 0
                else:
                    streak += 1
                    total += streak
            return total
        return countSubarrays(right) - countSubarrays(left - 1)
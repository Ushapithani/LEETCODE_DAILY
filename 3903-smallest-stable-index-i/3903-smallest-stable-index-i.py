class Solution:
    def firstStableIndex(self, nums, k):
        for i in range(len(nums)):
            left_max = max(nums[:i + 1])
            right_min = min(nums[i:])

            if left_max - right_min <= k:
                return i

        return -1
class Solution:
    def longestSubsequence(self, nums):
        n = len(nums)
        x = 0
        nz = False

        for a in nums:
            x ^= a

            if a != 0:
                nz = True

        if x != 0:
            return n

        if nz:
            return n - 1

        return 0
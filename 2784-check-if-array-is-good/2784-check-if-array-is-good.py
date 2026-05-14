class Solution:
    def isGood(self, nums):
        n = max(nums)

        if len(nums) != n + 1:
            return False

        freq = {}

        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        for i in range(1, n):
            if i not in freq or freq[i] != 1:
                return False

        return n in freq and freq[n] == 2
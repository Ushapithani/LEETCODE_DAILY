class Solution:
    def numSubarraysWithSum(self, nums, goal):
        count = {0: 1}
        prefix = 0
        result = 0
        for num in nums:
            prefix += num
            if prefix - goal in count:
                result += count[prefix - goal]
            if prefix in count:
                count[prefix] += 1
            else:
                count[prefix] = 1
        return result
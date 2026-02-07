class Solution:
    def rearrangeArray(self, nums):
        nums.sort()
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        
        for i in range(n):
            if i % 2 == 0:
                res[i] = nums[left]
                left += 1
            else:
                res[i] = nums[right]
                right -= 1
        return res
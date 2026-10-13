class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: x*x)
        half = len(nums)//2
        small = sum(x*x for x in nums[:half])
        large = sum(x*x for x in nums[half:])
        return large-small
        
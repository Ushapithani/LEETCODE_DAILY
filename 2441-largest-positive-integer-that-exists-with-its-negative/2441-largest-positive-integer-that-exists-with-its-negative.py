class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        seen = set(nums)
        ans = -1
        for num in nums :
            if num in seen and -num in seen :
                ans = max(num,ans)
        return ans 
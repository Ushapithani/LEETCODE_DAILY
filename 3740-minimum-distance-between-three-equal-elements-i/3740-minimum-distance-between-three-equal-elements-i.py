class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        ans = -1
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] and nums[j] == nums[k]:
                        dist = (j - i) + (k - j) + (k - i)
                        if ans == -1 or dist < ans:
                            ans = dist
        
        return ans
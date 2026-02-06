class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        max_window = 0
        for right in range(n):
            while nums[right] > k * nums[left]:
                left += 1
            max_window = max(max_window, right - left + 1)
        return n - max_window
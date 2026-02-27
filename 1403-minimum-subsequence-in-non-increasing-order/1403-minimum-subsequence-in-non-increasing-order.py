class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        totalSum = sum(nums)
        subsequence = []
        currentSum = 0
        for value in nums:
            subsequence.append(value)
            currentSum += value
            if currentSum > totalSum - currentSum:
                break
        return subsequence
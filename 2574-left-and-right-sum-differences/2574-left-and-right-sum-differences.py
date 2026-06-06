class Solution:
    def leftRightDifference(self, nums):
        ans = []

        leftSum = 0
        rightSum = sum(nums)

        for num in nums:
            rightSum -= num
            ans.append(abs(leftSum - rightSum))
            leftSum += num

        return ans
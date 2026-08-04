class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        return max(
            self.houseRobber(nums[:-1]),  
            self.houseRobber(nums[1:])    
        )

    def houseRobber(self, nums):
        if len(nums) == 1:
            return nums[0]

        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            next_money = max(curr, nums[i] + prev)
            prev = curr
            curr = next_money

        return curr
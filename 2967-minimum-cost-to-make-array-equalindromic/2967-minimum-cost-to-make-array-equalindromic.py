class Solution:
    def minimumCost(self, nums):
        nums.sort()
        n = len(nums)
        median = nums[n // 2]

        def isPalindrome(x):
            s = str(x)
            return s == s[::-1]

        def getPalindrome(num, d):
            while not isPalindrome(num):
                num += d
            return num

        low = getPalindrome(median, -1)
        high = getPalindrome(median, 1)

        def cost(x):
            return sum(abs(v - x) for v in nums)

        return min(cost(low), cost(high))
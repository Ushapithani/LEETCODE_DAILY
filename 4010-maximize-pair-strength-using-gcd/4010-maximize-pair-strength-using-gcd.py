class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        import math

        answer = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                gcd_value = math.gcd(nums[i], nums[j])

                strength = (nums[i] * nums[j]) // (gcd_value * gcd_value)

                answer = max(answer, strength)

        return answer
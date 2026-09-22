class Solution:
    def maxLength(self, nums: list[int]) -> int:
        import math

        n = len(nums)
        answer = 1

        for i in range(n):
            product = 1
            gcd_value = 0
            lcm_value = 1

            for j in range(i, n):
                product *= nums[j]

                gcd_value = math.gcd(gcd_value, nums[j])

                lcm_value = math.lcm(lcm_value, nums[j])

                if product == gcd_value * lcm_value:
                    answer = max(answer, j - i + 1)

        return answer
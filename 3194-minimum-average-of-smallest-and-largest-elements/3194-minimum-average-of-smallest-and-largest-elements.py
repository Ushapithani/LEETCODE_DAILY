class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()

        left = 0
        right = len(nums) - 1

        answer = (nums[left] + nums[right]) / 2

        while left < right:
            average = (nums[left] + nums[right]) / 2
            answer = min(answer, average)

            left += 1
            right -= 1

        return answer
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        remaining_elements = nums[1:]
        remaining_elements.sort()
        return first + remaining_elements[0] + remaining_elements[1]
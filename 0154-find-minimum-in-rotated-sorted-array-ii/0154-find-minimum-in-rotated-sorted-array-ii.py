
class Solution:
    def findMin(self, nums: List[int]) -> int:
        unique_elements = set(nums)
        return min(unique_elements)
        

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        present = set(nums)

        smallest = min(nums)
        largest = max(nums)

        ans = []

        for i in range(smallest, largest + 1):
            if i not in present:
                ans.append(i)

        return ans
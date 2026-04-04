class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        nums=sorted(nums,reverse=True)
        return sorted(nums,key=count.get)
        
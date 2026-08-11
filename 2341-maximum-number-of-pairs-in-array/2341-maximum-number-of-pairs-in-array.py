class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = {}
        pairs=0 
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for count in freq.values():
            pairs+= count//2
        leftover = len(nums)-pairs*2
        return [pairs,leftover]

        
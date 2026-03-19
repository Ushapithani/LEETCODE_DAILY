class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums)%p
        if remainder==0:
            return 0
        seen = {0:-1}
        prefix=0
        min_len=len(nums)
        for i,num in enumerate(nums):
            prefix=(prefix+num)%p
            target = (prefix-remainder)%p
            if target in seen:
                min_len=min(min_len,i-seen[target])
            seen[prefix]=i 
        if min_len<len(nums):
            return min_len
        else:
            return -1       
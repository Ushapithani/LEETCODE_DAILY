class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = {0:1}
        prefix = 0 
        result = 0 
        for num in nums :
            prefix +=num%2
            if prefix - k in count :
                result += count[prefix-k]
            if prefix in count  :
                count[prefix]+=1
            else:
                count[prefix]=1
        return result

        
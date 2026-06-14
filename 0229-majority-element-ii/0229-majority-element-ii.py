class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        result =[]
        n = len(nums)
        majority = n//3
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1 
        for num in freq:
            if freq[num]>majority:
                result.append(num)

        return result
        
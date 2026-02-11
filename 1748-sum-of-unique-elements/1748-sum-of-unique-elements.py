class Solution:
    def sumOfUnique(self, nums):
        freq = {} 
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        total = 0
        for num, count in freq.items():
            if count == 1:   
                total += num
        return total
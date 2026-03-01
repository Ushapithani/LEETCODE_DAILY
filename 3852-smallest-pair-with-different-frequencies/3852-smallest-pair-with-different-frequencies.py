from collections import Counter

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        
        distinct = sorted(freq.keys())  # sorted distinct values
        
        for i in range(len(distinct)):
            for j in range(i+1, len(distinct)):
                x = distinct[i]
                y = distinct[j]
                if freq[x] != freq[y]:
                    return [x, y]
        
        return [-1, -1]
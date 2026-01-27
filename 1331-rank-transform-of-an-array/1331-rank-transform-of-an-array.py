class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank = {}
        for i in range(len(sorted_unique)):
            rank[sorted_unique[i]] = i+1
        result = []
        for num in arr:   
            result.append(rank[num])
        return result
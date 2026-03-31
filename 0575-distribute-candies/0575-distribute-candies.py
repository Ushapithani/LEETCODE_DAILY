class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n= len(candyType)
        unique = len(set(candyType))
        return min(unique,n//2)


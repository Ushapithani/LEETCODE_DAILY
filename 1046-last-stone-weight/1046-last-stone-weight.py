class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            stones[-2] = stones[-1] - stones[-2]
            stones.pop()
        
        return stones[0] if stones else 0
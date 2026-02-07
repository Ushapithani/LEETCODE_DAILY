class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        diff = (sumA - sumB) // 2
        setB = set(bobSizes)
        
        for a in aliceSizes:
            if a - diff in setB:
                return [a, a - diff]


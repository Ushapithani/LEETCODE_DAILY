class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = {}   
        
        
        for row in grid:
            for num in row:
                if num in seen:
                    seen[num] += 1
                else:
                    seen[num] = 1
        
        repeated = missing = -1
        
        
        for i in range(1, n * n + 1):
            if i in seen and seen[i] == 2:
                repeated = i
            elif i not in seen:
                missing = i
        
        return [repeated, missing]
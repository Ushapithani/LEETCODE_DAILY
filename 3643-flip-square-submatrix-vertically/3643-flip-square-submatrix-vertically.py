class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(x, x + k // 2):
            mirror = x + k - 1 - (i - x)
            for j in range(y, y + k):
                grid[i][j], grid[mirror][j] = grid[mirror][j], grid[i][j]
        return grid
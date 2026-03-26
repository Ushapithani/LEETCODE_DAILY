class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        flat = sum(grid, [])
        k %= len(flat)

        flat.reverse()
        flat[:k] = flat[:k][::-1]
        flat[k:] = flat[k:][::-1]

        result = []
        for r in range(m):
            result.append(flat[r*n:(r+1)*n])
        return result
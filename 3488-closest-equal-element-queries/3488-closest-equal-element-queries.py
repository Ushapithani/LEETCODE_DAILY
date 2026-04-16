
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = 2 * n
        
        d = [m] * m
        
        last = {}
        for i in range(m):
            x = nums[i % n]
            if x in last:
                d[i] = min(d[i], i - last[x])
            last[x] = i
        
        last.clear()
        for i in range(m - 1, -1, -1):
            x = nums[i % n]
            if x in last:
                d[i] = min(d[i], last[x] - i)
            last[x] = i
        
        for i in range(n):
            d[i] = min(d[i], d[i + n])
        
        result = []
        for i in queries:
            if d[i] >= n:
                result.append(-1)
            else:
                result.append(d[i])
        
        return result
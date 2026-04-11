class Solution:
    def minimumDistance(self, nums):
        pos = {}
        for i, v in enumerate(nums):
            if v not in pos:
                pos[v] = []
            pos[v].append(i)
        
        ans = float('inf')
        for idxs in pos.values():
            for i in range(len(idxs) - 2):
                a, b, c = idxs[i], idxs[i+1], idxs[i+2]
                dist = abs(a-b) + abs(b-c) + abs(c-a)
                ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1
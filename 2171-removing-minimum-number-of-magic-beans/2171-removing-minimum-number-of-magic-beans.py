class Solution:
    def minimumRemoval(self, beans):
        beans.sort()
        total = sum(beans)
        n = len(beans)
        
        max_keep = 0
        
        for i in range(n):
            keep = beans[i] * (n - i)
            max_keep = max(max_keep, keep)
        
        return total - max_keep
class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        
        left = 0
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                left = j
                break
        
        right = 0
        for i in range(n):
            if colors[i] != colors[n - 1]:
                right = i
                break
        
        return max(left, (n - 1) - right)
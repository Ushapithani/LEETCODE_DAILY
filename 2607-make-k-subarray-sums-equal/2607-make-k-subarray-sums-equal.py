from math import gcd

class Solution:
    def makeSubKSumEqual(self, arr, k):
        n = len(arr)
        g = gcd(n, k)
        ans = 0
        
        for i in range(g):
            group = []
            j = i
            
            while True:
                group.append(arr[j])
                j = (j + k) % n
                if j == i:
                    break
            
            group.sort()
            median = group[len(group)//2]
            
            for x in group:
                ans += abs(x - median)
        
        return ans
from collections import defaultdict

class Solution:
    def distance(self, nums):
        d, res = defaultdict(list), [0]*len(nums)
        for i, x in enumerate(nums): d[x].append(i)
        for v in d.values():
            n, l, r = len(v), 0, sum(v)
            for i, x in enumerate(v):
                r -= x
                res[x] = x*i - l + (r - x*(n-i-1))
                l += x
        return res
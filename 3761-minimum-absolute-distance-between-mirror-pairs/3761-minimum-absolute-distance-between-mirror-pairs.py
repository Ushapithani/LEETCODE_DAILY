from collections import defaultdict

class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        want = defaultdict(int)
        seen = set()
        ans = float('inf')

        for i, v in enumerate(nums):
            if v in seen:
                ans = min(ans, i - want[v])
            rev = int(str(v)[::-1])
            want[rev] = i
            seen.add(rev)

        return ans if ans != float('inf') else -1
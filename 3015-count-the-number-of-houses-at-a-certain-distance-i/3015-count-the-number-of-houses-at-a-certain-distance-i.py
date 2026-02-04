class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        ans = [0] * n
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                
                direct = abs(i - j)
                via_xy = abs(i - x) + 1 + abs(y - j)
                via_yx = abs(i - y) + 1 + abs(x - j)
                
                dist = min(direct, via_xy, via_yx)
                ans[dist - 1] += 1
        
        return ans

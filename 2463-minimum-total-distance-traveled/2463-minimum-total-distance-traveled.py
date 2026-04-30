class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(i, j):
            # all robots assigned
            if i == len(robot):
                return 0
            
            if j == len(factory):
                return float('inf')
            
            res = dp(i, j + 1)  
            
            pos, cap = factory[j]
            dist = 0
            
            for k in range(cap):
                if i + k >= len(robot):
                    break
                
                dist += abs(robot[i + k] - pos)
                res = min(res, dist + dp(i + k + 1, j + 1))
            
            return res
        
        return dp(0, 0)
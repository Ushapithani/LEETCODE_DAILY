class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                children[m].append(i)
        
        def dfs(i):
            max_time = 0
            for child in children[i]:
                max_time = max(max_time, dfs(child))
            return informTime[i] + max_time
        
        return dfs(headID)
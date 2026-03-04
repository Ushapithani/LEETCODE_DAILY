class Solution:
    def findOrder(self, numCourses: int, prerequisites: list) -> list:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for a, b in prerequisites:
            graph[b].append(a)
        
        visited = set()
        cycle = set()
        result = []
        
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            cycle.remove(node)
            visited.add(node)
            result.append(node)
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return []
        
        return result[::-1]
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}

        def dfs(node, c):
            visited[node] = c
            for nei in graph[node]:
                if nei in visited:
                    if visited[nei] == c:
                        return False
                else:
                    if not dfs(nei, 1 - c):
                        return False
            return True

        for node in range(len(graph)):
            if node not in visited:
                if not dfs(node, 0):
                    return False
        return True
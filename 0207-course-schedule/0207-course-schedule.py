class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)

        visited = set()
        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            visiting.remove(node)
            visited.add(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
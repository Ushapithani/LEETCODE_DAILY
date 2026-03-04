class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        
        cloned = {}
        
        def dfs(node):
            if node in cloned:
                return cloned[node]
            clone = Node(node.val)
            cloned[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        
        return dfs(node)
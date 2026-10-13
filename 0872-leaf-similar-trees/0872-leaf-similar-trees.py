class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        mp1 = []
        mp2 = []
        def solve(node, mp):
            if not node:
                return 
            if not node.left and not node.right:
                mp.append(node.val)
            solve(node.left, mp)
            solve(node.right, mp)
        
        solve(root1,mp1)
        solve(root2,mp2)
        return mp1 == mp2
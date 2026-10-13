class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        mp1 = {}
        mp2 = {}
        def solve(node, mp):
            nonlocal cnt
            if node is None :
                return 
            if not node.left and not node.right:
                mp[cnt] = node.val
                cnt+=1
                return 
            solve(node.left, mp)
            solve(node.right, mp)
        
        cnt = 0
        solve(root1,mp1)
        cnt = 0
        solve(root2,mp2)
        return mp1 == mp2
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # left -> left(1) , 1+right
        # right -> 1+left , right(1)
        ...
        # left , right = 0,1
        ans = 0
        def solve(node, direction ,len):
            nonlocal ans
            if not node:
                return 
            ans = max(ans , len)
            if direction == 0: # left direction
                solve(node.right , 1 , len+1)
                solve(node.left , 0 , 1)
            else:
                solve(node.left , 0 , len+1)
                solve(node.right, 1, 1)
            
        solve(root , 0, 0)
        solve(root, 1, 0)
        return ans
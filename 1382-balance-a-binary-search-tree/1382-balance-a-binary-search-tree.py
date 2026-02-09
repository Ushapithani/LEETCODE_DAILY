
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        
        nums = inorder(root)
        
        def buildBST(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            node = TreeNode(arr[mid])   
            node.left = buildBST(arr[:mid])
            node.right = buildBST(arr[mid+1:])
            return node
        
        return buildBST(nums)
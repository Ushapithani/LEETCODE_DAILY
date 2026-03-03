class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            if targetSum == root.val:
                return True
            else:
                return False
        if root.left is not None:
            if self.hasPathSum(root.left, targetSum - root.val):
                return True
        if root.right is not None:
            if self.hasPathSum(root.right, targetSum - root.val):
                return True
        return False
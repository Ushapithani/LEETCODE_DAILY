class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def solve(node, maxi):
            if not node:
                return 0

            cnt = 0

            if node.val >= maxi:
                cnt += 1

            cnt += solve(node.left, max(maxi, node.val))
            cnt += solve(node.right, max(maxi, node.val))

            return cnt

        return solve(root, root.val)
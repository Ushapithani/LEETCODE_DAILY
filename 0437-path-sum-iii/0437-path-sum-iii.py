class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        mp = {0: 1}

        def dfs(node, curr):
            if not node:
                return 0

            curr += node.val
            cnt = mp.get(curr - targetSum, 0)

            mp[curr] = mp.get(curr, 0) + 1

            cnt += dfs(node.left, curr)
            cnt += dfs(node.right, curr)

            mp[curr] -= 1

            return cnt

        return dfs(root, 0)
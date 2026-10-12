
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        values = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        result = []
        max_count = 0
        i = 0

        while i < len(values):
            count = 1

            while i + count < len(values) and values[i] == values[i + count]:
                count += 1

            if count > max_count:
                max_count = count
                result = [values[i]]
            elif count == max_count:
                result.append(values[i])

            i += count

        return result

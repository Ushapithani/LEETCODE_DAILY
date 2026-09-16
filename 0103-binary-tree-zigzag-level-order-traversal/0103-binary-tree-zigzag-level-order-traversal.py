import collections

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        direction = 1
        deq = collections.deque([root])
        res = []

        while deq:
            level = []

            for i in range(len(deq)):
                node = deq.popleft()

                level.append(node.val)

                if node.left:
                    deq.append(node.left)

                if node.right:
                    deq.append(node.right)

            if direction % 2 == 0:
                res.append(level[::-1])
            else:
                res.append(level)

            direction += 1

        return res
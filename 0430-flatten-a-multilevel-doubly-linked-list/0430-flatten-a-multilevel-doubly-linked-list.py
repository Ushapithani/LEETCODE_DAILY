class Solution:
    def flatten(self, head):
        if not head:
            return head

        arr = []
        curr = head

        while curr:
            if curr.child:
                if curr.next:
                    arr.append(curr.next)

                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None

            elif curr.next is None and arr:
                node = arr.pop()
                curr.next = node
                node.prev = curr

            curr = curr.next

        return head
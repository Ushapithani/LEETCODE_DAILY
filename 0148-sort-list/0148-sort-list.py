class Solution(object):
    def sortList(self, head):
        values = []
        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next

        values.sort()

        curr = head
        i = 0

        while curr:
            curr.val = values[i]
            i += 1
            curr = curr.next

        return head
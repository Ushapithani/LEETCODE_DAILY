class Solution(object):
    def partition(self, head, x):
        small = []
        large = []

        curr = head

        while curr:
            if curr.val < x:
                small.append(curr.val)
            else:
                large.append(curr.val)

            curr = curr.next

        values = small + large

        curr = head
        i = 0

        while curr:
            curr.val = values[i]
            i += 1
            curr = curr.next

        return head
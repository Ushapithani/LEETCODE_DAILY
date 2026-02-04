class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head, k):
        first = head
        for _ in range(k-1):
            first = first.next

        fast = first
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next

        first.val, slow.val = slow.val, first.val
        return head
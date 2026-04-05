# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev_a=list1
        for i in range(a-1):
            prev_a=prev_a.next
        after_b= prev_a
        for i in range(b-a+2):
            after_b=after_b.next
        prev_a.next = list2
        tail=list2
        while tail.next:
            tail=tail.next
        tail.next=after_b
        return list1




        
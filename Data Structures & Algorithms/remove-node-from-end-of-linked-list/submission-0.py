# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        start = ListNode(0)
        start.next = head
        prev = start
        curr = head
        while length > n:
            length -= 1
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return start.next
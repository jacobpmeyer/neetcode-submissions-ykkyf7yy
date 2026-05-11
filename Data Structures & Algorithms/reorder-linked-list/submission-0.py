# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        before = []
        curr = head
        while curr:
            before.append(curr)
            curr = curr.next

        after = [before[0]]
        i = 1
        while len(after) < len(before):
            if len(after) % 2 == 0:
                after.append(before[i])
                i += 1
            else:
                after.append(before[-i])

        for i in range(len(after) - 1):
            after[i].next = after[i + 1]
        after[-1].next = None
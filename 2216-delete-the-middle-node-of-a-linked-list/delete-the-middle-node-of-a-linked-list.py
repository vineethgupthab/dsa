# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h1 = head
        original_head = h1
        h2 = head
        prev = None
        while h2 and h2.next:
            prev = h1
            h1 = h1.next
            h2 = h2.next.next
        
        if prev:
            prev.next = h1.next
        else:
            original_head = original_head.next

        return original_head

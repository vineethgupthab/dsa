# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n==0:
            return head.next
        cursor = head
        array = []
        while cursor:
            array.append(cursor)
            cursor = cursor.next
        
        if n==len(array):
            return head.next
        
        n = len(array)-n-1
        cursor = head; output = cursor; i=0
        while cursor:
            if i==n:
                cursor.next = cursor.next.next
                i+=1
                break
            cursor = cursor.next
            i+=1
        return output
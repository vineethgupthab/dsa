# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n1 = head
        n2 = head
        n1_vals = []
        while n2!=None:
            n1_vals.append(n1.val)
            n2 = n2.next.next
            n1 = n1.next
        '''n2_vals = []
        while n1!=None:
            n2_vals.append(n1.val)
            n1 = n1.next
        n2_vals = n2_vals[::-1]
        return max([n1_vals[i]+n2_vals[i] for i in range(len(n1_vals))])'''
        
        max_sum = 0
        while n1!=None:
            temp = n1_vals.pop()
            max_sum = max(max_sum, temp+n1.val)
            n1 = n1.next
        return max_sum
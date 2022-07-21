# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, m, n):
        if m == n: return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m-1):
            pre = pre.next
            
        curr = pre.next
        nxt = curr.next
        
        for i in range(n-m):
            tmp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = tmp
            
        pre.next.next = nxt
        pre.next = curr
        return dummy.next
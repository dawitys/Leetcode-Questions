# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ans = pre = ListNode(0)
        
        dummy = ListNode(0) 
        dummy.next = head
        curr = head = dummy
        while(curr and curr.next):
            if curr.next.val < x:
                pre.next =curr.next
                pre = pre.next
                
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        pre.next = head.next
            
        return ans.next
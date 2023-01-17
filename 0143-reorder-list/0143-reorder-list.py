# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None
        
        def reverse(node):
            if(not node or not node.next):
                return node
            rev = reverse(node.next)
            node.next.next = node
            node.next = None
            return rev
        
        head1 = head
        head2 = reverse(head2)
        
        while(head1 and head2):
            head1.next, head1   = head2,head1.next
            head2.next, head2 = head1, head2.next
            
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            s=head
            f=head.next

            while s is not f:
                s=s.next
                f=f.next.next

            return True
        except AttributeError:
            return False
    
        
        
        
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
        if not head or not head.next:
            return

        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        curr = s.next
        s.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        l_0 = head
        l_n = prev

        while l_n:
            temp1 = l_0.next
            temp2 = l_n.next

            l_0.next = l_n
            l_n.next = temp1

            l_0 = temp1
            l_n = temp2

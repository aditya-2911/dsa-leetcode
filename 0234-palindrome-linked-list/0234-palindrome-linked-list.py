# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s,f=head,head
        data=[]
        ct=0
        while f and f.next:
            data.append(s.val)
            ct+=2
            s=s.next
            f=f.next.next
  
        if f:
            s=s.next
        i=len(data)-1

        while s and i>=0:
            if s.val!=data[i]:
                return False
            i-=1
            s=s.next
        return True
        

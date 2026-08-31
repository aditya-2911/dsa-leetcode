# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        curr=prev.next

        first,last=-1,-1
        j=i=2
        min_dist=10**5+1

        while curr.next:
            nxt=curr.next
            if ((curr.val<prev.val) and (curr.val<nxt.val)) or ((curr.val>prev.val) and (curr.val>nxt.val)):
                if first==-1:
                    first=i
                else:
                    if i-last<min_dist:
                        min_dist=i-last
                last=i
            
            
            prev=curr
            curr=nxt
            i+=1

        if first==last:
            return [-1,-1]

        return [min_dist,last-first]
        
            
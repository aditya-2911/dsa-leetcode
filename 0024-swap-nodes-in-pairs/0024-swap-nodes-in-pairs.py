# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head, times):
            curr = head
            prev = None
            while times:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

                times -= 1

        if head is None:
            return head

        left = head
        res = None
        prevLeft = None

        while True:
            right = left
            for i in range(1):
                if right is None:
                    break
                right = right.next

            if right:
                nextLeft = right.next
                reverse(left, 2)

                if prevLeft:
                    prevLeft.next = right
                prevLeft = left

                if res is None:
                    res = right
                left = nextLeft
            else:
                if prevLeft:
                    prevLeft.next = left

                if res is None:
                    res = left

                break
        return res

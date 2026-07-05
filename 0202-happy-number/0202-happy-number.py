class Solution:
    def isHappy(self, n: int) -> bool:

        def digitSquare(num):
            s=0
            while num>0:
                s+=(num%10)**2
                num//=10
            return s
        
        slow=n
        fast=n

        while fast!=1:
            slow = digitSquare(slow)
            fast = digitSquare(fast)
            fast = digitSquare(fast)

            if slow == fast and slow!=1:
                return False
        return True
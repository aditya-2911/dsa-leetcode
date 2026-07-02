class Solution:
    def mirrorDistance(self, n: int) -> int:
        ans=0
        num=n
        while n>0:
            ans=ans*10 + (n%10)
            n//=10

        return abs(num-ans)